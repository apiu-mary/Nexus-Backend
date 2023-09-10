from django.urls import path
from .views import UnitSharingList

urlpatterns = [
    path("sharing/" ,UnitSharingList.as_view(), name= "unit_sharing_list"),
]

