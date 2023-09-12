from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from meter_reading.models import MeterReading
from .serializers import MeterReadingSerializer

# Create your tests here.

class MeterReadingListTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.meter_reading_data = {'reading': 100}

    def create_meter_reading(self):
        return MeterReading.objects.create(reading=self.meter_reading_data['reading'])

    def test_create_meter_reading(self):
        response = self.client.post(reverse('meter-reading-list'), self.meter_reading_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MeterReading.objects.count(), 1)

    def test_get_meter_reading_list(self):
        self.create_meter_reading()
        response = self.client.get(reverse('meter-reading-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_meter_reading_detail(self):
        meter_reading = self.create_meter_reading()
        response = self.client.get(reverse('meter-reading-detail', args=[meter_reading.pk]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_meter_reading(self):
        meter_reading = self.create_meter_reading()
        updated_data = {'reading': 200}
        response = self.client.put(reverse('meter-reading-detail', args=[meter_reading.pk]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        meter_reading.refresh_from_db()
        self.assertEqual(meter_reading.reading, updated_data['reading'])

    def test_delete_meter_reading(self):
        meter_reading = self.create_meter_reading()
        response = self.client.delete(reverse('meter-reading-detail', args=[meter_reading.pk]), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MeterReading.objects.count(), 0)
