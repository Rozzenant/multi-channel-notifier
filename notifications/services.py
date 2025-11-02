from django.core.mail import send_mail
import requests
import os


def send_email(notif):
    send_mail(
        "Уведомление",
        notif.message,
        os.getenv("EMAIL_HOST_USER"),
        [notif.user.email],
    )


def send_sms(notif):
    phone = notif.user.profile.phone
    api_id = os.getenv("SMS_API_KEY")
    url = os.getenv("SMS_URL", "https://sms.ru/sms/send")
    data = {"api_id": api_id, "to": phone, "msg": notif.message, "json": 1}
    response = requests.post(url, data=data)
    if response.status_code != 200:
        raise Exception(
            f"SMS.ru returned status code {response.status_code}: {response.text}"
        )
    result = response.json()
    print(result)


def send_telegram(notif):
    tg_id = notif.user.profile.telegram_id
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data={"chat_id": tg_id, "text": notif.message})
