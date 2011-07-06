from django.conf.urls.defaults import *
from django.contrib.gis import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	#(r'^admin/(.*)', admin.site.root),
	(r'^explore', 'sanfran.views.explore'),	
	(r'^explore/$', 'sanfran.views.explore'),
    # Example:
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),	
)
