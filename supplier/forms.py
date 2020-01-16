from django import forms
from supplier.models import *

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        exclude = ['date']