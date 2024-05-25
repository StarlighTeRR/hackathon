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

FROM build as release

WORKDIR /app

# Копирование собранного проекта из предыдущего этапа
COPY --from=build /app/dist ./dist
COPY --from=build /app/package*.json ./

# Установка сервера (например, serve) для обслуживания статических файлов
RUN npm install -g serve

# Открытие порта
EXPOSE 3030

# Команда для запуска сервера
CMD ["serve", "-s", "dist", "-l", "3030"]