from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SharingSerializer
from unit_sharing.models import UnitSharing
# Create your views here.


class UnitSharingList(APIView):
    def get(self,request):
        unit_sharing = UnitSharing.objects.all()
        serializer = SharingSerializer(unit_sharing,many=True)
        return Response(serializer.data)
     # The endpoint is supposed to to retrieve a list of all UnitSharing objects.
    # Its typically used to fetch data from server,like displaying a list of shared units
     

    def post(self,request):
        serializer = SharingSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    # The post method is supposed to handle POST requests.This endpoint meant to create a new
    # unit sharing object. Its used when a customer adds a new shared unit into the system


class UnitSharingDetail(APIView):
     def get_object(self, pk):
        try:
            return UnitSharing.objects.get(pk=pk)
        except UnitSharing.DoesNotExist:
            raise Http404
        

     def get(self, request, pk):
        unit = self.get_object(pk)
        serializer = SharingSerializer(unit)
        return Response(serializer.data)
     

     def put(self, request, pk):
        unit = self.get_object(pk)
        serializer = SharingSerializer(unit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

     def delete(self, request, pk):
        unit = self.get_object(pk)
        unit.delete()
        return Response("Unit record deleted",status=status.HTTP_204_NO_CONTENT)