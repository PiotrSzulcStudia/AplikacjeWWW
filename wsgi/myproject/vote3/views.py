# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import RequestContext

from .models import District, Commission
from .forms import CommissionForm

# Create your views here.
def index(request):
    voievodships = District.objects.filter(parentId=None)
    context = {'voievodships': voievodships}
    return render(request, 'vote3/index.html', context)

def district_view(request, district_id, error='', success=''):
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

    context = {'voievodships': districts,'commissions': commissions, 'breadcrumbs': breadcrumbs, 'error': error, 'success': success}
    return render(request, 'vote3/index.html', context)


def commission(request):
    context = RequestContext(request)
    commission_id = None
    if request.method == 'GET':
        commission_id = request.GET['commission_id']
        commission = Commission.objects.get(pk=int(commission_id))
        return JsonResponse({'voters': commission.votersAllowedToVote,
        'cards': commission.receivedCardsToVote,
        'timesModificated': commission.timesModificated})

    elif request.method == 'POST':
        commission_id = int(request.POST['commission_id'])
        postTimesModificated = int(request.POST['times_modificated'])
        commission = Commission.objects.get(pk=commission_id)

        if (postTimesModificated != commission.timesModificated):
            return JsonResponse({ 'status': 'error',
                    'error_type': 'modification',
                    'error_msg': "Ktoś zmodyfikował już ten wpis"
            })


        cards = int(request.POST['cards'])
        voters = int(request.POST['voters'])

        if (cards < 0 or voters < 0):
            return JsonResponse({ 'status': 'error',
                'error_type': "negative",
                'error_msg': "Ujemne wartości"
            })

        commission.receivedCardsToVote = int(request.POST['cards'])
        commission.votersAllowedToVote = int(request.POST['voters'])
        commission.timesModificated = commission.timesModificated + 1
        commission.save()

        return JsonResponse({ 'status': 'ok',
            'id': commission.id,
            'cards': commission.receivedCardsToVote,
            'voters': commission.votersAllowedToVote,
            'timesModificated': commission.timesModificated
        })
