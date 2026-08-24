FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=drf.settings

RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instalar drf-yasg explícitamente
RUN pip install drf-yasg==1.21.7

COPY . .

RUN mkdir -p /app/media /app/static

EXPOSE 8090

CMD ["gunicorn", "drf.wsgi:application", "--bind", "0.0.0.0:8090"]