from django.conf.urls.defaults import *
from django.contrib.gis import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	#(r'^admin/', include(admin.site.urls)),
	(r'^admin/(.*)', admin.site.root),
	(r'^explore', 'sanfran.views.explore'),	
	(r'^explore/$', 'sanfran.views.explore'),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),
    (r'^admin_media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.ADMIN_MEDIA_PREFIX
    }),	
    # Example:
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),	
)
