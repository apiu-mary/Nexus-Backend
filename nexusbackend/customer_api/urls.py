from django.urls import path
from .views import CustomerDetailView, CustomerListView

urlpatterns = [
    path ("Customer/",CustomerListView.as_view(), name = "customer_list_view"),
    path("Customer/<int:id>/",CustomerDetailView.as_view(), name = "customer_detail_view"),
]