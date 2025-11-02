FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential curl netcat gcc && \
    pip install --upgrade pip && \
    apt-get clean

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "notifier.wsgi:application", "--bind", "0.0.0.0:8000"]
