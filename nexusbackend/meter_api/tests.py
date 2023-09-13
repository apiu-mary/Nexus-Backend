import uuid
from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from meter.models import Meter

class MeterTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.meter_data = {
            "current_reading": "50.0",
            "status": "active"
        }
        self.meter = Meter.objects.create(**self.meter_data)
        self.url_list = reverse("MeterListView")
        self.url_detail = reverse("MeterDetailsview", args=[self.meter.pk])

    def test_list_meters(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_meter(self):
        response = self.client.post(self.url_list, self.meter_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Meter.objects.count(), 2)

    def test_get_meter_details(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

  

    def test_update_meter_details(self):
        updated_data = {
            "current_reading": "60.0",
            "status": "inactive"
        }
        response = self.client.put(self.url_detail, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.meter.refresh_from_db()
        self.assertEqual(float(self.meter.current_reading), 60.0)

    def test_update_nonexistent_meter_details(self):
        nonexistent_url = reverse("MeterDetailsview", args=[999])
        response = self.client.put(nonexistent_url, self.meter_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_meter(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Meter.objects.count(), 0)

 