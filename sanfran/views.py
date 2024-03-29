import logging
from django.template import Context, loader
from django.http import HttpResponse
from sanfran.models import PlanningNeighborhoods

log = logging.getLogger(__name__)

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

def about(request):
    t = loader.get_template('sanfran/about.html')
    c = Context()
    return HttpResponse(t.render(c))
