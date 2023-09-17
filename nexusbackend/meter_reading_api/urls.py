from django.urls import path
from .views import MeterList, MeterReadingList, MeterReadingDetail

urlpatterns = [
    path('meters/', MeterList.as_view(), name='meter-list'),
    path('meter-readings/', MeterReadingList.as_view(), name='meter-reading-list'),
    path('meter-readings/<int:pk>/', MeterReadingDetail.as_view(), name='meter-reading-detail'),
]
