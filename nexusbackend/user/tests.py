from dataclasses import make_dataclass
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from faker import Faker  # Import the Faker library
from .models import CustomUser
from .serializers import CustomUserSerializer


class UserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = '/api/user/register/'  
        self.login_url = '/api/user/login/'        
        self.fake = Faker() 
        
    def test_user_registration(self):
        fake_data = {
            "email": self.fake.email(),
            "name": self.fake.name(),
            "city": self.fake.city(),
            "phonenumber": self.fake.phone_number(),
            "password": self.fake.password(),
            "confirm_password": self.fake.password()
    }
        
    response = self.client.post(self.register_url, fake_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(CustomUser.objects.count(), 1)


        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(CustomUser.objects.count(), 1)

    def test_user_login(self):
        user_data = {
            "email": "user@example.com",
            "name": "Test User",
            "city": "Test City",
            "phonenumber": "+1234567890",
            "password": "testpassword",
            "confirm_password": "testpassword"
        }
        CustomUser.objects.create(**user_data)

        user_data = {
            "email": "user@example.com", 
            "password": "testpassword"  
        }
        response = self.client.post('/login/', data={'email': 'email', 'password': 'password'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
     
  
