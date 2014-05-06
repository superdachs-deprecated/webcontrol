from django.shortcuts import render
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from network_base.models import NetworkInterface, Hostname

def index(request):
    nics = NetworkInterface.objects.all()
    hostname = Hostname.objects.all()[0]
    context = { 'nics': nics,
                'hostname': hostname,
    }
    return render(request, 'network_base/index.phtml', context)

