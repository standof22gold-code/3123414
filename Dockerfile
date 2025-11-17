FROM python:3.9-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Создаем необходимые папки
RUN mkdir -p logs storage/cache storage/plugins storage/products configs plugins

# Открываем порт (если нужен веб-интерфейс)
EXPOSE 8080

# Запускаем бота
CMD ["python", "main.py"]
