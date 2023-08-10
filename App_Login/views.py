from django.shortcuts import render,HttpResponse
from django.urls import reverse

# authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate




# Create your views here.
