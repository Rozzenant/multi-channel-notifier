from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Notification, UserProfile


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "id",
            "user",
            "message",
            "status",
            "channels_tried",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["status", "channels_tried", "created_at", "updated_at"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["phone", "telegram_id"]


class UserCreateSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(write_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "profile"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.update_or_create(user=user, defaults=profile_data)
        return user
