from rest_framework import serializers
from unit_sharing.models import UnitSharing

class SharingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitSharing
        fields = "shared_units, updated_at, created_at"