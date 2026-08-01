FROM python:3.11-slim

WORKDIR /app

# تثبيت متطلبات النظام
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# نسخ المتطلبات وتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي كود المشروع
COPY . .

# أمر تشغيل البوت الأساسي
CMD ["python", "main.py"]
