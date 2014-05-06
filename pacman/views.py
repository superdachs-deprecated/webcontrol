from django.shortcuts import render
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from pacman.models import Repository

def index(request):
    repos = Repository.objects.all()
    context = { 'repos': repos,}
    return render(request, 'pacman/index.phtml', context)
