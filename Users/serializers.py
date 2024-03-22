from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    gravatar = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = 'id', 'username', 'email', 'role', "first_name", "last_name", "password", "gravatar", "is_verified", "is_active"
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def get_gravatar(self, obj):
        request = self.context.get('request')
        if (request is None):
            print("Request is None")
            return "None"
        else:
            size = 150
            return obj.gravatar_image(size)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        password = validated_data.get('password')
        return user

    def update(self, instance, validated_data):
        # Remove password from validated data
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)  # Call parent's update method
        if password:  # Check if password is provided
            instance.set_password(password)  # Set new password if provided
            instance.save()
        return instance
