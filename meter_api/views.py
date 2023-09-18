
from django.shortcuts import render
from rest_framework.views import APIView
from meter.models import Meter
from rest_framework.response import Response
from rest_framework import status
from meter_api.serializers import MeterSerializer
from rest_framework.exceptions import NotFound, ValidationError

class MeterListView(APIView):
    def get(self, request):
        status_filter = request.query_params.get('status')
        if status_filter:
            meters = Meter.objects.filter(status=status_filter)
        else:
            meters = Meter.objects.all()

        serializer = MeterSerializer(meters, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MeterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            raise ValidationError("Invalid data provided for meter creation.")

class MeterDetailsView(APIView):
    def get(self, request, pk):
        try:
            meter = Meter.objects.get(pk=pk)
        except Meter.DoesNotExist:
            raise NotFound("Meter not found.")

        serializer = MeterSerializer(meter)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            meter = Meter.objects.get(pk=pk)
        except Meter.DoesNotExist:
            raise NotFound("Meter not found.")

        meter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        try:
            meter = Meter.objects.get(pk=pk)
        except Meter.DoesNotExist:
            raise NotFound("Meter not found.")

        serializer = MeterSerializer(meter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            raise ValidationError("Invalid data provided for meter update.")

     
