from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, request, response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import *
from django.views import View
from django.conf import settings
# Create your views here.

def home(request):
    return render(request,'base.html')