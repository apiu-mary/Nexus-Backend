from django.shortcuts import get_object_or_404, render
from meter_reading.models import MeterReading
from .serializers import MeterReadingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class MeterReadingList(APIView):
    def get(self, request, pk=None, format=None):
        try:
            if pk is not None:
                meter_reading = get_object_or_404(MeterReading, pk=pk)
                serializer = MeterReadingSerializer(meter_reading)
                return Response(serializer.data)
            else:
                meter_readings = MeterReading.objects.all()
                serializer = MeterReadingSerializer(meter_readings, many=True)
                return Response(serializer.data)
        except MeterReading.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def post(self, request, format=None):
        serializer = MeterReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk, format=None):
        try:
            meter_reading = MeterReading.objects.get(pk=pk)
            serializer = MeterReadingSerializer(meter_reading, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MeterReading.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, pk, format=None):
        try:
            meter_reading = MeterReading.objects.get(pk=pk)
            meter_reading.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MeterReading.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
