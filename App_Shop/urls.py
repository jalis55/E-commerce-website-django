from django.urls import path
from App_Shop import views

app_name="App_Shop"

urlpatterns=[
    path("",views.Home.as_view(),name="home"),
    path("product-details/<pk>",views.ProductDetaits.as_view(),name="product_details"),


]