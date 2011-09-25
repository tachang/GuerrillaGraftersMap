from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.gis.gdal import SpatialReference, CoordTransform
from django.contrib.gis.geos import Point, GEOSGeometry

from sanfran.models import PlanningNeighborhoods
from sanfran.models import Trees

import logging

log = logging.getLogger(__name__)
gcoord = SpatialReference('EPSG:4326')
mycoord = SpatialReference('EPSG:900913')
trans = CoordTransform(gcoord, mycoord)

def explore(request):
    #neighborhoods = PlanningNeighborhoods.objects.all()
    neighborhoods = []

    #for neighborhood in neighborhoods:
    #    neighborhood.geom.transform(900913)

    t = loader.get_template('sanfran/explore.html')
    c = Context({
        'neighborhoods': neighborhoods,
    })

    return HttpResponse(t.render(c))

def add_tree(request):
	if request.method == 'POST':
		lat = request.POST['lat']
		lon = request.POST['lon'] 
		latlon = (float(lon), float(lat))
		point = Point(latlon, srid=4326).transform(trans, clone=True)
		tree = Trees(common_name="test tree", geom=point)
		tree.save()
		return HttpResponseRedirect('/add/')
	else:
		c = {}
		tree_points = []
		trees = Trees.objects.all()		
		for tree in trees:
			tree.geom.transform(4326)
			pnt = GEOSGeometry(tree.geom.wkt) # WKT
			tree_points.append(pnt)
		c.update(dict(points=tree_points))			
		c.update(csrf(request))
		log.info(c)
		return render_to_response("sanfran/add_tree.html", c)
	
	return render_to_response(t.render(rc))

def about(request):
    t = loader.get_template('sanfran/about.html')
    c = Context()
    return HttpResponse(t.render(c))
