from django.shortcuts import render
from django.http import HttpResponse

from .models import District, Commission

# Create your views here.
def index(request):
    voievodships = District.objects.filter(parentId=None)
    context = {'voievodships': voievodships}
    return render(request, 'vote2/index.html', context)
