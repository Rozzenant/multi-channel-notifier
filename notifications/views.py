from rest_framework import viewsets
from .models import Notification
from .serializers import NotificationSerializer
from .tasks import send_notification_task_real as send_notification_task

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def perform_create(self, serializer):
        notif = serializer.save()
        send_notification_task.delay(notif.id)
