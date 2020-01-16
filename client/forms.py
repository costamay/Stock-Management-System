from django import forms
from client.models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
             'client_name','client_phone','product' 
        )
        

