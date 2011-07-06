# Guerilla Grafters Fabric Deployment File
# Please do not copy

from fabric.api import *

"""
Base configuration
"""
env.project_name = 'guerillagrafters'
env.database_password = '5IQZe7WEix'
env.site_media_prefix = "site_media"
env.admin_media_prefix = "admin_media"
env.path = '/home/newsapps/sites/%(project_name)s' % env
env.log_path = '/home/newsapps/logs/%(project_name)s' % env
env.env_path = '%(path)s/env' % env
env.repo_path = '%(path)s/repository' % env
env.apache_config_path = '/home/newsapps/sites/apache/%(project_name)s' % env
env.python = 'python2.6'
env.repository_url = 'git://github.com/boundsj/GuerrillaGraftersMap.git'
# TODO: enable server caching
env.multi_server = False
# env.memcached_server_address = "cache.example.com"

"""
Environments
"""
def production():
    """
    TBD
    """

def staging():
    """
    Work on staging environment
    """
    env.settings = 'staging'
	# "newsapps" user is due to the fact that our EC2 (Amazon web serivce) server was set up from 
	# the chicago tribune open source, ec2, geodjango project's ec2 build image
    env.user = 'newsapps' 
    env.hosts = ['ec2-184-73-123-132.compute-1.amazonaws.com'] 
    # Install your SSH public key in the 'authorized_keys' file for the above user on the above host,
    # or specify the path to your private key in env.key_filename below.
    # see http://www.eng.cam.ac.uk/help/jpmg/ssh/authorized_keys_howto.html for more info.
    # env.key_filename = 'path_to_your_key_file.pem'
    env.s3_bucket = 'rebounds-dev'

"""
Branches
"""
def master():
    """
    Work on development branch.
    """
    env.branch = 'master'

def branch(branch_name):
    """
    Work on any specified branch.
    """
    env.branch = branch_name

"""
Commands - setup
"""
def setup():
    """
    Setup a fresh virtualenv, install everything we need, and fire up the database.

    Does NOT perform the functions of deploy().
    """
    require('settings', provided_by=[production, staging])
    require('branch', provided_by=[master, branch])

    setup_directories()
    setup_virtualenv()
    clone_repo()
    checkout_latest()
    destroy_database()
    create_database()
    load_data()
    install_requirements()
    maintenance_down()

def setup_directories():
    """
    Create directories necessary for deployment.
    """
    run('mkdir -p %(path)s' % env)
    run('mkdir -p %(env_path)s' % env)
    run ('mkdir -p %(log_path)s;' % env)
    sudo('chgrp -R www-data %(log_path)s; chmod -R g+w %(log_path)s;' % env)
    run('ln -s %(log_path)s %(path)s/logs' % env)

def setup_virtualenv():
    """
    Setup a fresh virtualenv.
    """
    run('virtualenv -p %(python)s --no-site-packages %(env_path)s;' % env)
    run('source %(env_path)s/bin/activate; easy_install -U setuptools; easy_install pip;' % env)

def clone_repo():
    """
    Do initial clone of the git repository.
    """
    run('git clone %(repository_url)s %(repo_path)s' % env)

def checkout_latest():
    """
    Pull the latest code on the specified branch.
    """
    run('cd %(repo_path)s; git checkout %(branch)s; git pull origin %(branch)s' % env)

def install_requirements():
    """
    Install the required packages using pip.
    """
    run('source %(env_path)s/bin/activate; pip install -E %(env_path)s -r %(repo_path)s/requirements.txt' % env)

def install_apache_conf():
    """
    Install the apache site config file.
    """
    sudo('cp %(repo_path)s/configs/%(settings)s/apache %(apache_config_path)s' % env)

def maintenance_up():
    """
    Install the Apache maintenance configuration.
    """
    sudo('cp %(repo_path)s/%(project_name)s/configs/%(settings)s/apache_maintenance %(apache_config_path)s' % env)
    reboot()

def maintenance_down():
    """
    Reinstall the normal site configuration.
    """
    install_apache_conf()
    reboot()

"""
Commands - deployment
"""
"""
Commands - deployment
"""
def deploy():
    """
    Deploy the latest version of the site to the server and restart Apache2.
    
    Does not perform the functions of load_new_data().
    """
    require('settings', provided_by=[production, staging])
    require('branch', provided_by=[master, branch])
            
    checkout_latest()
    gzip_assets()
    deploy_to_s3()
    maintenance_down()

def gzip_assets():
    """
    GZips every file in the assets directory and places the new file
    in the gzip directory with the same filename.
    """
    run('cd %(repo_path)s; python gzip_assets.py' % env)

def deploy_to_s3():
    """
    Deploy the latest project site media to S3.
    """
    env.gzip_path = '%(path)s/repository/%(project_name)s/gzip/assets/' % env
    run(('s3cmd -P --add-header=Content-encoding:gzip --guess-mime-type --rexclude-from=%(path)s/repository/s3exclude sync %(gzip_path)s s3://%(s3_bucket)s/%(project_name)s/%(admin_media_prefix)s/') % env)

def reboot(): 
    """
    Restart the Apache2 server.
    """
    if env.multi_server:
        run('/mnt/apps/bin/restart-all-apache.sh')
    else:
        sudo('service apache2 restart')

"""
Commands - data
"""
# def load_new_data():
#     """
#     Erase the current database and load new data from the SQL dump file.
#     """
#     require('settings', provided_by=[production, staging])
# 
#     maintenance_up()
#     pgpool_down()
#     destroy_database()
#     create_database()
#     load_data()
#     pgpool_up()
#     maintenance_down()

def load_data():
    """
    Loads data from the repository into PostgreSQL.
    """
    run('psql -q %(project_name)s < %(path)s/repository/sanfran/data/database/dump.sql' % env)
    run('psql -q %(project_name)s < %(path)s/repository/sanfran/data/database/finish_init.sql' % env)

def create_database(func=run):
    """
    Creates the user and database for this project.
    """
    func('echo "CREATE USER %(project_name)s WITH PASSWORD \'%(database_password)s\';" | psql postgres' % env)
    func('createdb -O %(project_name)s %(project_name)s -T template_postgis' % env)

def destroy_database(func=run):
    """
    Destroys the user and database for this project.

    Will not cause the fab to fail if they do not exist.
    """
    with settings(warn_only=True):
        func('dropdb %(project_name)s' % env)
        func('dropuser %(project_name)s' % env)

def pgpool_down():
    """
    Stop pgpool so that it won't prevent the database from being rebuilt.
    """
    sudo('/etc/init.d/pgpool stop')

def pgpool_up():
    """
    Start pgpool.
    """
    sudo('/etc/init.d/pgpool start')

"""
Deaths, destroyers of worlds
"""
def shiva_the_destroyer():
    """
    Remove all directories, databases, etc. associated with the application.
    """
    with settings(warn_only=True):
        run('rm -Rf %(path)s' % env)
        run('rm -Rf %(log_path)s' % env)
        pgpool_down()
        run('dropdb %(project_name)s' % env)
        run('dropuser %(project_name)s' % env)
        pgpool_up()
        sudo('rm %(apache_config_path)s' % env)
        reboot()
        run('s3cmd del --recursive s3://%(s3_bucket)s/%(project_name)s' % env)
