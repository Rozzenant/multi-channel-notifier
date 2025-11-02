from rest_framework import viewsets, generics
from .models import Notification
from .serializers import NotificationSerializer, UserCreateSerializer
from .tasks import send_notification_task_real as send_notification_task
from django.contrib.auth.models import User

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def perform_create(self, serializer):
        notif = serializer.save()
        send_notification_task.delay(notif.id)

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
