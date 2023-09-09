from django.shortcuts import render
from meter_reading.models import MeterReading
from .serializers import MeterReadingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class MeterReadingList(APIView):
    def get(self, request, format=None):
        meter_readings = MeterReading.objects.all()
        serializer = MeterReadingSerializer(meter_readings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MeterReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

