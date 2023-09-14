from django.test import TestCase
from django.db.utils import IntegrityError 
from .models import MeterReading
from django.utils import timezone

class MeterReadingTestCase(TestCase):
    def setUp(self):
        self.reading_data = {
            'current_reading': 100.50,
            'date': '2023-09-12',
        }

    def test_create_meter_reading(self):
        meter_reading = MeterReading.objects.create(**self.reading_data)
        self.assertEqual(meter_reading.current_reading, self.reading_data['current_reading'])
        self.assertEqual(str(meter_reading), f"Meter Reading - Date: {self.reading_data['date']}, Current Reading: {self.reading_data['current_reading']}")

    def test_create_meter_reading_without_date(self):
        reading_data_without_date = self.reading_data.copy()
        del reading_data_without_date['date']
        with self.assertRaises(IntegrityError):
            MeterReading.objects.create(**reading_data_without_date)

    def test_create_meter_reading_without_current_reading(self):
        reading_data_without_reading = self.reading_data.copy()
        del reading_data_without_reading['current_reading']
        with self.assertRaises(IntegrityError):
            MeterReading.objects.create(**reading_data_without_reading)

    def test_create_meter_reading_with_default_date(self):
        reading_data_with_default_date = {
            'current_reading': 100.50,
        }
        meter_reading = MeterReading.objects.create(
            **reading_data_with_default_date,
            date=timezone.now().date()
        )
        self.assertEqual(meter_reading.current_reading, reading_data_with_default_date['current_reading'])
