from django import forms
from sales.models import *

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sale
        exclude = ['date']

