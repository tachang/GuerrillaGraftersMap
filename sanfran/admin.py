from django.contrib.gis import admin
from models import PlanningNeighborhoods, Trees

admin.site.register(PlanningNeighborhoods, admin.OSMGeoAdmin)
geoAdmin = admin.OSMGeoAdmin
geoAdmin.default_lon=-13630737.0
geoAdmin.default_lat=4545793.0
geoAdmin.default_zoom=12
admin.site.register(Trees, geoAdmin)
