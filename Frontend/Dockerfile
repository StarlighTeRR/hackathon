# Этап 1: Сборка JSON из YAML
FROM node:lts-alpine3.20 as build

ARG TASK_BINARY=task_linux_amd64.tar.gz

RUN apk update && apk add --no-cache \
    build-base \
    npm \
    && rm -rf /var/cache/apk/*

WORKDIR /app

RUN npm set progress=false

COPY package*.json .

RUN npm install @vue/cli -g
RUN npm install

COPY . .

RUN npm run build

# Этап 2: Запуск сервера
FROM nginx:alpine as release

# Удаляем дефолтный файл конфигурации Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Копируем наш файл конфигурации Nginx
COPY nginx.conf /etc/nginx/conf.d

# Копирование собранного проекта из предыдущего этапа
COPY --from=build /app/dist /usr/share/nginx/html

# Открытие порта
EXPOSE 3030

# Запуск Nginx
CMD ["nginx", "-g", "daemon off;"]