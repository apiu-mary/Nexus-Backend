from django.http import Http404
from django.shortcuts import render
from meter_reading.models import MeterReading
from .serializers import MeterReadingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class MeterReadingList(APIView):
    def get_object(self, pk):
        try:
            return MeterReading.objects.get(pk=pk)
        except MeterReading.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk is not None:
            meter_reading = self.get_object(pk)
            serializer = MeterReadingSerializer(meter_reading)
            return Response(serializer.data)
        else:
            meter_readings = MeterReading.objects.all()
            serializer = MeterReadingSerializer(meter_readings, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MeterReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            meter_reading = MeterReading.objects.get(pk=pk)
        except MeterReading.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MeterReadingSerializer(meter_reading, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            meter_reading = MeterReading.objects.get(pk=pk)
        except MeterReading.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        meter_reading.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
