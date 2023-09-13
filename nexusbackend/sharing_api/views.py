from django.http import Http404
from rest_framework .decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SharingSerializer
from unit_sharing.models import UnitSharing
# Create your views here.

@api_view(['GET','POST'])
def sharing_list(request):
    if request.method =='GET':
     device= UnitSharing.objects.all()
     serializer= SharingSerializer(device,many=True )
     return Response(serializer.data)
    if request.method == 'POST':
       serializer = SharingSerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def sharing_detail(request, id):
    try:
        sharing = UnitSharing.objects.get(pk=id)

        if request.method == 'GET':
            serializer = SharingSerializer(sharing)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = SharingSerializer(sharing, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Units successfully edited",
                        "device_data": serializer.data
                    }
                )
            else:
                return Response(
                    {
                        "error": "Invalid data",
                        "errors": serializer.errors,
                        "message": "Failed to update unit sharing details"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
    except UnitSharing.DoesNotExist:
        return Response(
            {"error": "Units not found", "message": "The requested shared units do not exist"},
            status=status.HTTP_404_NOT_FOUND
        )

