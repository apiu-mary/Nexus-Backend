from django.urls import path
from .views import MeterListView

urlpatterns = [
    path("meter/", MeterListView.as_view(), name="MeterListView"),
]
