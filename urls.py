from django.conf.urls.defaults import *
from django.contrib.gis import admin

admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'^explore', 'sanfran.views.explore'),	
	(r'^explore/$', 'sanfran.views.explore'),
    # Example:
    # (r'^GiraffeGraftersMap/', include('GiraffeGraftersMap.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),	
)
