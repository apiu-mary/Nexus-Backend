from django.test import TestCase
from django.contrib.auth import get_user_model
from phonenumber_field.phonenumber import PhoneNumber
from django.contrib.contenttypes.models import ContentType
from .models import CustomUser


class CustomUserTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser1',
            'email': 'testuser@example.com',
            'name': 'Test User',
            'city': 'Test City',
            'phonenumber': PhoneNumber.from_string('+1234567890'),
            'password': 'testpassword',
            'confirm_password': 'testpassword',
        }

    def test_create_custom_user(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertIsInstance(user, CustomUser)
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])
        self.assertEqual(user.name, self.user_data['name'])
        self.assertEqual(user.city, self.user_data['city'])
        self.assertEqual(user.phonenumber, self.user_data['phonenumber'])

    def test_create_superuser(self):
        superuser = CustomUser.objects.create_superuser(**self.user_data)
        self.assertIsInstance(superuser, CustomUser)
        self.assertEqual(superuser.username, self.user_data['username'])
        self.assertEqual(superuser.email, self.user_data['email'])
        self.assertEqual(superuser.name, self.user_data['name'])
        self.assertEqual(superuser.city, self.user_data['city'])
        self.assertEqual(superuser.phonenumber, self.user_data['phonenumber'])
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_create_user_with_blank_fields(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(username='', email='', name='', 
                                           city='', phonenumber=None, password='')

 

    def test_string_representation(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertEqual(str(user), self.user_data['username'])

 
    def test_create_user_with_different_email(self):
        CustomUser.objects.create_user(**self.user_data)
        user = CustomUser.objects.create_user(username='anotheruser', 
                                              email='another@example.com', 
                                              name='Another User', 
                                              city='Another City', 
                                              phonenumber=PhoneNumber.
                                              from_string
                                              ('+9876543210'), 
                                              password='anotherpassword')
        self.assertEqual(user.email, 'another@example.com')

    def test_user_does_not_have_permissions(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertFalse(user.user_permissions.filter
                         (name='Test Permission').exists())
