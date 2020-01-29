from django import forms
from login.models import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['groups','email','name','password','is_staff']
