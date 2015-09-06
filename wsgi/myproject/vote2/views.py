from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import District, Commission
from .forms import CommissionForm

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

def commision_view(request, commission_id):
    formError =''
    commission = Commission.objects.get(pk=commission_id)
    if request.method == 'POST':
        form = CommissionForm(request.POST)

        if form.is_valid():

            formTimesModificated = form.cleaned_data['timesModificated']
            curTimesModificated = commission.timesModificated

            if curTimesModificated > formTimesModificated:
                formError = 'Nieaktualne dane'
                return render(request, 'vote2/commission.html', {'form': form, 'formError': formError})

            formVoters = form.cleaned_data['votersAllowedToVote']
            formCards = form.cleaned_data['receivedCardsToVote']

            if ((formVoters < 0) or (formCards < 0)):
                formError = 'Ujemne dane'
                return render(request, 'vote2/commission.html', {'form': form, 'formError': formError})

            commission.receivedCardsToVote = formCards
            commission.votersAllowedToVote = formVoters
            commission.timesModificated = curTimesModificated + 1
            commission.save()

            return HttpResponseRedirect('./')

    else:
        form = CommissionForm(initial={"receivedCardsToVote": commission.receivedCardsToVote,
            "votersAllowedToVote": commission.votersAllowedToVote,
            "timesModificated": commission.timesModificated
        })

    return render(request, 'vote2/commission.html', {'form': form, 'formError': formError, 'commission': commission})
