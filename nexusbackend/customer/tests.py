# from django.test import TestCase
# from customer.models import Customer
# class UserModelTest(TestCase):
#     def setUp(self):
#         self.user = Customer.objects.create(
#             company_name='Nexus',
#             phone='+123456789',
#             city ='123 Main St',
#             country='password'
#         )
#     def test_user_creation(self):
#         # Retrieve the user from the database
#         user = Customer.objects.get(username='john')
#         # Assert that the user was created successfully
#         self.assertEqual(user.phone, '+123456789')
#         self.assertEqual(user.city, '123 Main St')
#         self.assertEqual(user.company_name, 'password')
#     def test_user_str_representation(self):
#         # Assert that the __str__ method returns the username
#         self.assertEqual(str(self.user), 'john')