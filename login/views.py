from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect

from django.contrib.auth import login,authenticate
from login.models import *
from django.contrib.auth.decorators import login_required,user_passes_test
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import REDIRECT_FIELD_NAME


# Create your views here.
