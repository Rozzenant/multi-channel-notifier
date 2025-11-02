# Multi-Channel Notifier

**Multi-Channel Notifier** — это система надёжной доставки уведомлений пользователям через Email, Telegram и SMS с fallback-механизмом. Если отправка через один канал не удалась, пробуются остальные.

Проект реализован как **тестовое задание для Photo Point**.

---

## Стек технологий

- Python 3.10+
- Django 4.x
- Django REST Framework
- Celery
- Redis
- SQLite (можно заменить на PostgreSQL)
- Docker / Docker Compose

---

## Задача, которую решает система

Система уведомлений решает задачу надёжной доставки сообщений клиентам компании по разным каналам связи:

- Сначала пробуется Email.
- Если неудачно — Telegram.
- Если и он не сработал — SMS.
- Поддерживается статус отправки и отслеживание каналов, через которые уже была попытка.

---

## Быстрый старт (локально, без Docker)

1. Клонировать репозиторий:

```bash
git clone https://github.com/Rozzenant/multi-channel-notifier.git
cd multi-channel-notifier
```

2. Создайте виртуальное окружение:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Скопируйте .env.example и заполните переменные:
```bash
cp .env.example .env
```

5. Примените миграции и создайте суперпользователя:
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. Запустите сервер:
```bash
python manage.py runserver
```

7. Запустите Celery (на Windows)
```bash
celery -A notifier worker --pool=solo -l info
```

8. Установите и запустите redis:

Скачать архив с Redis отсюда:
https://github.com/tporadowski/redis/releases

Затем из папки redis запустите:
```bash
redis-server.exe redis.windows.conf
```

## Быстрый запуск через Docker

1. Клонируйте репозиторий и перейдите в папку:

```bash
git clone https://github.com/Rozzenant/multi-channel-notifier.git
cd multi-channel-notifier
```

2. Скопируйте .env файл:
```bash
cp .env.example .env
```

3. Запустите приложение через Docker Compose:
```bash
docker-compose up --build
```

Приложение будет доступно (Docker):
Django API: http://localhost:25100
Django Admin: http://localhost:25100/admin

Приложение будет доступно (Локально):
Django API: http://localhost:8000
Django Admin: http://localhost:8000/admin

## Тестирование через Postman
1. Откройте файл test.postman_collection.json в Postman







