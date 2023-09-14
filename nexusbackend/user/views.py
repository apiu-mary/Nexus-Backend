from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class UserListView(APIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
   

@api_view(['POST'])
def user_login_view(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, 
                            status=status.HTTP_401_UNAUTHORIZED)
        if user.check_password(password):
            return Response({'message': 'Successfully logged in.'}, 
                            status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, 
                            status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
def user_logout_view(request):
    if request.method == 'POST':
        logout(request)
        return Response({'message': 'Successfully logged out.'}, 
                        status=status.HTTP_200_OK)
@api_view(['POST'])
def user_registration_view(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({'message': 'Successfully registered'}, 
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)