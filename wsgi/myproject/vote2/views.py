from django.shortcuts import render
from django.http import HttpResponse

from .models import District, Commission

# Create your views here.
def index(request):
    voievodships = District.objects.filter(parentId=None)
    context = {'voievodships': voievodships}
    return render(request, 'vote2/index.html', context)

def district_view(request, district_id):
    districts = District.objects.filter(parentId=district_id)
    commissions = Commission.objects.filter(parentId=district_id)
    v = District.objects.get(pk=district_id)
    breadcrumbs = []
    while v.parentId:
        breadcrumbs.append(v)
        v = District.objects.get(pk=v.parentId.id)
    if v:
        breadcrumbs.append(v)

    breadcrumbs.reverse()

    context = {'voievodships': districts,'commissions': commissions, 'breadcrumbs': breadcrumbs}
    return render(request, 'vote2/index.html', context)
