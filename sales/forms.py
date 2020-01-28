from django import forms
from sales.models import *

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sale
        exclude = ['date']

class DateRangeForm(forms.Form):
    start_date =forms.DateField()
    end_date = forms.DateField()

