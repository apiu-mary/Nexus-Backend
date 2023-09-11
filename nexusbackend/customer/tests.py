from django.test import TestCase
from customer.models import Customer

class UserModelTest(TestCase):
    def setUp(self):
        self.user = Customer.objects.create(
            company_name='Nexus',
            phone='+123456789',
            city ='123 Main St',
            country='password'
        )
    def test_user_creation(self):
        
        user = Customer.objects.get(username='Nexus')
       
        self.assertEqual(user.phone, '+123456789')
        self.assertEqual(user.city, '123 Main St')
        self.assertEqual(user.company_name, 'password')
    def test_user_str_representation(self):
        
        self.assertEqual(str(self.user), 'Nexus') 