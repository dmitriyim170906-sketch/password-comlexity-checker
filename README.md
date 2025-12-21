# Password Complexity Checker
CLI-утилита и Web API для оценки сложности паролей по заданным критериям.

## Архитектура
* `src/checker.py` — ядро логики оценки.
* `src/main.py` — CLI-интерфейс (argparse).
* `src/api.py` — Web API на FastAPI.
* `src/config.py` — конфигурация.

## Локальный запуск (заполню позже)

##  Запуск в Docker

### Способ 1: Используя Docker Compose (рекомендуется)

# Собрать и запустить
docker-compose up -d

# Остановить
docker-compose down

# Просмотр логов
docker-compose logs -f

### Способ 1: Используя Docker напрямую

# Собрать образ
docker build -t password-checker .

# Запустить контейнер
docker run -d -p 8000:8000 --name checker-app password-checker

# Остановить контейнер
docker stop checker-app
docker rm checker-app
Проверка работы

## Конфигурация (заполню позже)
## Примеры использования (заполню позже)