# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class PlanningNeighborhoods(models.Model):
    objectid = models.FloatField()
    neighborho = models.CharField(max_length=25)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()


    class Meta:
		verbose_name_plural = "Planning Neighborhoods"
    
    def __unicode__(self):
		return self.neighborho


