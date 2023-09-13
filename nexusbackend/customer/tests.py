from django.test import TestCase
from customer.models import Customer


class UserModelTest(TestCase):
    def setUp(self):
        self.user = Customer.objects.create(
            company_name='Nexus',
            phone_number='+123456789',
            city='123 Main St',
            country='password'
        )
        
    def test_user_creation(self):
        
        user = Customer.objects.get(company_name='Nexus')
       
        self.assertEqual(user.phone_number, '+123456789')
        
        self.assertEqual(user.city, '123 Main St')
        self.assertEqual(user.country, 'password')
             
    def test_user_str_representation(self):
        
        self.assertEqual(str(self.user), 'Nexus')
      
    def tearDown(self):
        self.user.delete()
