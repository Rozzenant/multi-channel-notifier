from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Notification(models.Model):
    STATUS_CHOICES = [
        ("pending", "В ожидании"),
        ("sent", "Отправлено"),
        ("failed", "Ошибка"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    channels_tried = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=20, blank=True)
    telegram_id = models.CharField(max_length=50, blank=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
