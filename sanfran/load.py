import os
from django.contrib.gis.utils import LayerMapping
from models import PlanningNeighborhoods

# Auto-generated `LayerMapping` dictionary for PlanningNeighborhoods model
planningneighborhoods_mapping = {
    'objectid' : 'OBJECTID',
    'neighborho' : 'NEIGHBORHO',
    'geom' : 'MULTIPOLYGON',
}

sanfran_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/planning_neighborhoods.shp'))

def run(verbose=True):
	lm = LayerMapping(PlanningNeighborhoods, sanfran_shp, planningneighborhoods_mapping,
			transform=True, encoding='iso-8859-1')
			
	lm.save(strict=True, verbose=verbose)	
	
# cum = PlanningNeighborhoods.objects.get(neighborho='Castro/Upper Market')
# cum.geom.transform(900913)
# cum.geom.wkt

			