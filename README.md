<<<<<<< HEAD
# Password Complexity Checker
CLI-утилита и Web API для оценки сложности паролей по заданным критериям.

## Архитектура
* `src/checker.py` — ядро логики оценки.
* `src/main.py` — CLI-интерфейс (argparse).
* `src/api.py` — Web API на FastAPI.
* `src/config.py` — конфигурация.

## Локальный запуск 

# 1. Клонируйте репозиторий
git clone https://github.com/dmitriyim170906-sketch/password-comlexity-checker.git
cd password-complexity-checker

# 2. Создайте виртуальное окружение
python -m venv venv

# 3. Активируйте окружение
# Windows:
venv\Scripts\activate
# Linux/Mac:
# source venv/bin/activate

# 4. Установите зависимости
pip install -r requirements.txt

# 5. Запустите CLI
python src/main.py --password "Test123!"

# 6. Запустите API
python src/api.py
# Откройте: http://localhost:8000/docs

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

## Конфигурация 

Настройка через переменные окружения:
Скопируйте шаблон настроек:

bash
copy .env.example .env
Отредактируйте .env файл:

env
# Основные настройки
DEBUG=true
LOG_LEVEL=INFO
API_PORT=8000
API_HOST=0.0.0.0

# Критерии проверки паролей
MIN_PASSWORD_LENGTH=8
REQUIRE_DIGITS=true
REQUIRE_UPPERCASE=true
REQUIRE_LOWERCASE=true
REQUIRE_SPECIAL_CHARS=true
SPECIAL_CHARS=!@#$%^&*()_+-=[]{}|;:,.<>?`~

## 🛠 Инструменты разработки

### Качество кода
Проект использует современные инструменты для поддержания качества кода:

# Форматирование кода
black src tests
isort src tests

# Линтинг
ruff check src tests --fix
flake8 src tests

# Проверка типов
mypy src

# Тестирование
pytest tests/ -v
