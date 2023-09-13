from  rest_framework import serializers
from meter_reading.models import MeterReading

class MeterReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterReading
        fields = '__all__'