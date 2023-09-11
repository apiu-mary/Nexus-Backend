
from django.shortcuts import render
from rest_framework.views import APIView
from meter.models import Meter
from rest_framework.response import Response
from rest_framework import status

from meter_api.serializers import MeterSerializer

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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            meter = Meter.objects.get(pk=pk)
        except Meter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        meter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        try:
            meter = Meter.objects.get(pk=pk)
        except Meter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MeterSerializer(meter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

