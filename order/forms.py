from django import forms
from order.models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        
