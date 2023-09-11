import statistics
# from cairo import STATUS_CLIP_NOT_REPRESENTABLE, STATUS_DEVICE_ERROR, STATUS_DEVICE_FINISHED
from django.shortcuts import render
# from requests import Response
from rest_framework.views import APIView
from meter.models import Meter
from rest_framework.response import Response
from rest_framework import status
from .serializers import MeterSerializer

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
            return Response(serializer.data, status=STATUS_CLIP_NOT_REPRESENTABLE.HTTP_201_CREATED)
        return Response(serializer.errors, status=STATUS_DEVICE_FINISHED.HTTP_400_BAD_REQUEST)
