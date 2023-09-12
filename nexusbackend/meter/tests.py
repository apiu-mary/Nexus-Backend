
from django.test import TestCase
from .models import Meter

class MeterModelTestCase(TestCase):
    def setUp(self):
        self.meter = Meter.objects.create(
            meter_serial_number="A2023",
            current_reading=1000,
            status="Active"
        )

    # def test_meter_str_method(self):
    #     expected_str = str(self.meter.current_reading)
    #     self.assertEqual(str(self.meter), expected_str)

    def test_meter_serial_number_max_length(self):
        max_length = self.meter._meta.get_field('meter_serial_number').max_length
        self.assertEqual(max_length, 50)

    def test_current_reading_positive_integer(self):
        self.assertIsInstance(self.meter.current_reading, int)
        self.assertTrue(self.meter.current_reading >= 0)

    def test_status_max_length(self):
        max_length = self.meter._meta.get_field('status').max_length
        self.assertEqual(max_length, 32)
