from django import views
from django.urls import path
from .views import UnitSharingDetail, UnitSharingList

urlpatterns = [
    path("sharing/" ,UnitSharingList.as_view(), name= "unit_sharing_list"),
    path('sharing/<int:pk>/', UnitSharingDetail.as_view(), name='unit_sharing_detail'),
    path('sharing_api/sharing/<int:pk>/', UnitSharingDetail.as_view(), name='unit_sharing_detail'),


]

