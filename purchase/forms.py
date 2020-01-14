from django import forms
from purchase.models import *

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        exclude = ['date']

class UpdatePurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        exclude = ['date',]
