from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "name",
            "role",
            "password",
            "password2",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password and Confirm Password do not match."}
            )
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

