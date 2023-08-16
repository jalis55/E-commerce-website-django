from django.shortcuts import render
# models
from App_Shop.models import Product
from django.contrib.auth.mixins  import LoginRequiredMixin
# class based views
from django.views.generic import ListView,DetailView

# Create your views here.

class Home(ListView):
    model=Product
    template_name='App_Shop/home.html'

class ProductDetaits(DetailView):
    model=Product
    template_name='App_Shop/product_details.html'

