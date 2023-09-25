from rest_framework import serializers
from .models import CustomUser
from phonenumber_field.serializerfields import PhoneNumberField

class CustomUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    phonenumber = PhoneNumberField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phonenumber', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}, 'confirm_password': {'write_only': True}}

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password')
        if validated_data['password'] != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
