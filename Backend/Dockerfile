# Stage 1: Сборка проекта (установка зависимостей)
FROM python:3.12-slim AS build

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копируем файлы с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Запуск сервера Flask
FROM build as release

WORKDIR /app

# Копируем 
COPY --from=build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=build /usr/local/bin /usr/local/bin
COPY . .

# Устанавливаем переменную среды для указания Flask на то, что он должен запуститься в production mode
ENV FLASK_ENV=production

VOLUME /app/db.sqlite
EXPOSE 5000

# Запускаем сервер Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
