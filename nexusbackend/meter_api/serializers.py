from rest_framework import serializers
from meter.models import Meter

class MeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meter
        fields = '__all__'
