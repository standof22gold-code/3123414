FROM python:3.11-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копирование файлов
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Создание необходимых директорий
RUN mkdir -p configs logs storage/cache storage/plugins storage/products plugins

# Переменные окружения
ENV PYTHONUNBUFFERED=1
ENV FPC_IS_RUNNIG_AS_SERVICE=1

# Запуск
CMD ["python", "main.py"]