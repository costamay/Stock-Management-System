from django import forms
from login.models import *
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['groups','email','name','password','is_staff']
    # def get_form_kwargs(self):
    #     # update super call if python < 3
    #     form_kwargs = super().get_form_kwargs()
    #     form_kwargs['data'][''] = form_kwargs['data']['str_field_name'].lower()

    #     return form_kwargs