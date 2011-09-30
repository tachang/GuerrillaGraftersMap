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

class Tree(models.Model):
    location = models.CharField(max_length = 100)
    common_name = models.CharField(max_length = 100)
    scientific_name = models.CharField(max_length = 100)
    climate = models.ForeignKey('Climate')
    direction = models.ForeignKey('Direction') 
    moisture = models.ForeignKey('MoistureType')
    wind_type = models.ForeignKey('WindType')
    soil_type = models.ForeignKey('SoilType')
    sun_exposure = models.ForeignKey('SunExposure')
    native_to = models.CharField(max_length = 100)
    species = models.CharField(max_length = 100)
    variety = models.CharField(max_length = 100)
    span = models.DecimalField(max_digits = 5, decimal_places = 2)
    height = models.DecimalField(max_digits = 5, decimal_places = 2)
    status = models.CharField(max_length = 25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
		db_table = 'trees'
    
class Climate(models.Model):
    climate_description = models.TextField()

    class Meta:
		db_table = 'climates'
    
class Direction(models.Model):
    direction_description = models.TextField()

    class Meta:
		db_table = 'directions'
    
class MoistureType(models.Model):
    exposure_description = models.TextField() # should this be moisture_type_description?
    
    class Meta:
		db_table = 'moisture_types'
    
class WindType(models.Model):
    exposure_description = models.TextField() # should this be wind_type_description?

    class Meta:
		db_table = 'wind_types'
    
class SoilType(models.Model):
    exposure_description = models.TextField() # should this be soil_type_description?

    class Meta:
		db_table = 'soil_types'

class SunExposure(models.Model):
    exposure_description = models.TextField() # should this be sun_exposure_description?
    
    class Meta:
		db_table = 'sun_exposures'

class TreeEvent(models.Model):
    tree = models.ForeignKey(Tree)
    event_type = models.ForeignKey('TreeEventType')
    note = models.TextField()
    entered_by = models.ForeignKey('User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    
    class Meta:
		db_table = 'tree_events'

class TreeEventType(models.Model):
    event_type = models.CharField(max_length = 25)
    
    class Meta:
		db_table = 'tree_event_types'

class Visit(models.Model):
    date = models.DateField()
    grafter = models.ForeignKey('User')
    tree = models.ForeignKey('Tree')
    care_type = models.ForeignKey('CareType')
    gleaning = models.ForeignKey('Gleaning')
    grafting = models.ForeignKey('Grafting')
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
		db_table = 'visits'

class CareType(models.Model):
    care_type = models.CharField(max_length = 25)
    care_type_discription = models.TextField()

    class Meta:
		db_table = 'care_types'


class Gleaning(models.Model):
    amount_description = models.TextField()
    use = models.ForeignKey('UseType')
    planned_distribution = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
		db_table = 'gleanings'

class UseType(models.Model):
    use_name = models.CharField(max_length = 25)
    use_description = models.TextField()

    class Meta:
		db_table = 'use_types'

class Grafting(models.Model):
    note = models.TextField()
    method = models.ForeignKey('GraftMethod')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
		db_table = 'graftings'

class GraftMethod(models.Model):
    method_name = models.CharField(max_length = 25)
    method_description = models.TextField()

    class Meta:
		db_table = 'graft_methods'

class Steward(models.Model):
    tree = models.ForeignKey('Tree')
    user = models.ForeignKey('User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
		db_table = 'stewards'

class User(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    email = models.EmailField()
    phone = models.CharField(max_length = 12) # TODO: add validation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
		db_table = 'users'



