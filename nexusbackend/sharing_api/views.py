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
    

    def post(self,request):
        serializer = SharingSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
