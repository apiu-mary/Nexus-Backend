# from django.test import TestCase
# from django.utils import timezone
# from unit_sharing.models import UnitSharing
# from datetime import timedelta

# class UnitSharingModelTestCase(TestCase):
#     def test_model_creation(self):
#         shared_units = 10.5
#         created_at = timezone.now()
#         updated_at = timezone.now()

#         unit_sharing = UnitSharing.objects.create(
#             shared_units=shared_units,
#             created_at=created_at,
#             updated_at=updated_at,
#         )

#         self.assertIsInstance(unit_sharing, UnitSharing)
#         self.assertEqual(unit_sharing.shared_units, shared_units)
#         self.assertAlmostEqual(unit_sharing.created_at, created_at, delta=timedelta(milliseconds=10))  
#         self.assertAlmostEqual(unit_sharing.updated_at, updated_at, delta=timedelta(milliseconds=10))  

#     def test_model_str_representation(self):
#         shared_units = 7.25
#         created_at = timezone.now()
#         updated_at = timezone.now()

#         unit_sharing = UnitSharing(
#             shared_units=shared_units,
#             created_at=created_at,
#             updated_at=updated_at,
#         )

#         expected_str = f"Shared Units: {shared_units}, Created At: {created_at}, Updated At: {updated_at}"
#         self.assertEqual(str(unit_sharing), expected_str)

#     def test_max_digits_constraint(self):
#        with self.assertRaises(Exception) as context:
#            UnitSharing.objects.create(shared_units=12345.6789)
#        self.assertIn("A field with precision 4, scale 2 must round to an absolute value less than 10^2.", str(context.exception))

