from rest_framework import serializers
from unit_sharing.models import UnitSharing

class SharingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitSharing
        fields = "__all__"