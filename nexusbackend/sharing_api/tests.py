from django.test import TestCase
from django.utils import timezone
from unit_sharing.models import UnitSharing
# Create your tests here.

class UnitSharingModelTestCase(TestCase):
    def test_model_creation(self):
        shared_units = 10.5
        created_at = timezone.now()
        updated_at = timezone.now()
        
        unit_sharing = UnitSharing.objects.create(
            shared_units=shared_units,
            created_at=created_at,
            updated_at=updated_at,
        )
        
        self.assertIsInstance(unit_sharing, UnitSharing)
        self.assertEqual(unit_sharing.shared_units, shared_units)
        self.assertEqual(unit_sharing.created_at, created_at)
        self.assertEqual(unit_sharing.updated_at, updated_at)

    def test_model_str_representation(self):
        shared_units = 7.25
        created_at = timezone.now()
        updated_at = timezone.now()

        unit_sharing = UnitSharing(
            shared_units=shared_units,
            created_at=created_at,
            updated_at=updated_at,
        )
        expected_str = f"Shared Units: {shared_units}, Created At: {created_at}, Updated At: {updated_at}"
        self.assertEqual(str(unit_sharing), expected_str)


    def test_max_digits_constraint(self):
        with self.assertRaises(Exception) as context:
            UnitSharing.objects.create(shared_units=12345.6789)
        self.assertIn(str(context.exception))

