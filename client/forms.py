from django import forms
from client.models import *

class ClientForm(models.Model):
    class Meta:
        model = Client
        fields = "__all__"
        