from django.urls import path
from .views import MeterDetailsView, MeterListView


urlpatterns = [
    path("meter/", MeterListView.as_view(), name="MeterListView"),
    path("meter/<int:pk>/", MeterDetailsView.as_view(), name="MeterDetailsview"),
 
 
   
]
