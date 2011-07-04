from django.contrib.gis import admin
from models import PlanningNeighborhoods

admin.site.register(PlanningNeighborhoods, admin.OSMGeoAdmin)
