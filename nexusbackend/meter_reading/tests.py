from django.test import TestCase
from meter_reading.models import MeterReading

# Create your tests here.
class MeterReadingTestCase(TestCase):
    def setUp(self):
        #  tests data for my model
        self.reading1 = MeterReading.objects.create(current_reading=100.50, date='2023-09-12')
        self.reading2 = MeterReading.objects.create(current_reading=150.75, date='2023-09-13')

    def test_meter_reading_str_method(self):
        # Tests the __str__ method of the MeterReading model
        self.assertEqual(
            str(self.reading1),
            "Meter Reading - Date: 2023-09-12, Current Reading: 100.50"
        )
        self.assertEqual(
            str(self.reading2),
            "Meter Reading - Date: 2023-09-13, Current Reading: 150.75"
        )
