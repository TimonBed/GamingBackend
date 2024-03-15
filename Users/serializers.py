from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = 'id', 'username', 'email', 'role', "first_name", "last_name", "password"
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        password = validated_data.get('password')
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)  # Remove password from validated data
        instance = super().update(instance, validated_data)  # Call parent's update method
        if password:  # Check if password is provided
            instance.set_password(password)  # Set new password if provided
            instance.save()
        return instance