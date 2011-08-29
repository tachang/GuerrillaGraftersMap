from django.conf.urls.defaults import *
from django.contrib.gis import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^public/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': settings.STATIC_ROOT }),


    (r'^admin/', include(admin.site.urls)),
    (r'^explore/$', 'sanfran.views.explore'),
    (r'^about/$', 'sanfran.views.about'),
    (r'^$', 'sanfran.views.explore'),
	# temporary: to view static files on jesse's dev machine
	# (r'^public/(?P<path>.*)$', 'django.views.static.serve',
	#        {'document_root': '/Users/jesse/Documents/github/ggrafters_tachang/GuerrillaGraftersMap/public'}),	
    # Example:
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),	
)
