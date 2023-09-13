from django.urls import path
from .views import MeterReadingList

urlpatterns = [
    path('meter-readings/', MeterReadingList.as_view(), name='meter-reading-list'),
    path('meter-readings/<int:pk>/', MeterReadingList.as_view(), name='meter-reading-detail')

]
