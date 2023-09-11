from django.urls import path,re_path
from .views import CustomerDetailView, CustomerListView
from django.contrib import admin



urlpatterns = [
    path ("Customer/",CustomerListView.as_view(), name = "customer_list_view"),
    path("Customer/<int:id>/",CustomerDetailView.as_view(), name = "customer_detail_view"),
    
]