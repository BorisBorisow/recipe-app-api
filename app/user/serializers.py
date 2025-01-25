"""
Serializers for the user API View
"""

from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ["email", "password", "name"]
        extra_fields = {"passwort": {write_only: True, "min_length": 5}}

    def create(self, validated_data):
        """ Create a new user with encrypted password."""
        return get_user_mode().objects.create(**validated_data)
