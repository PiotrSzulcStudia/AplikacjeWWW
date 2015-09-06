# -*- coding: utf-8 -*-

from django import forms

class CommissionForm(forms.Form):
    receivedCardsToVote = forms.IntegerField(label='Otrzymano kart', required=True)
    votersAllowedToVote = forms.IntegerField(label='Uprawnionych do głosowania', required=True)
    timesModificated = forms.IntegerField(widget = forms.HiddenInput())
