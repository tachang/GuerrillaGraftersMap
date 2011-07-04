from django.template import Context, loader
from django.http import HttpResponse

def explore(request):
	t = loader.get_template('sanfran/explore.html')
	c = Context()
	return HttpResponse(t.render(c))
