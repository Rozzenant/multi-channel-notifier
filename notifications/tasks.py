from celery import shared_task
from .models import Notification
from .services import send_email, send_sms, send_telegram
import traceback

CHANNELS = ["email", "telegram", "sms"]


@shared_task(bind=True, max_retries=3, name="send_notification_task_real")
def send_notification_task_real(self, notif_id):
    notif = Notification.objects.get(id=notif_id)
    for channel in CHANNELS:
        if channel in notif.channels_tried:
            continue
        try:
            if channel == "email":
                send_email(notif)
            elif channel == "telegram":
                send_telegram(notif)
            elif channel == "sms":
                send_sms(notif)
            notif.status = "sent"
            notif.channels_tried.append(channel)
            notif.save()
            return
        except Exception as e:
            print(f"Ошибка при отправке через {channel}: {e}")
            traceback.print_exc()
            notif.channels_tried.append(channel)
            notif.save()
    notif.status = "failed"
    notif.save()
