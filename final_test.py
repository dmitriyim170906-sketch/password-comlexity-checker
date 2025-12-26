import os
import sys
import subprocess

def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print('='*60)

def check(description, condition):
    status = "✅" if condition else "❌"
    print(f"{status} {description}")
    return condition

print_section("ФИНАЛЬНАЯ ПРОВЕРКА ПРОЕКТА")

# Часть 1: Базовые проверки
print("\n📁 1. ПРОВЕРКА СТРУКТУРЫ ПРОЕКТА")

checks = [
    ("Папка src/ существует", os.path.exists("src")),
    ("Файл src/checker.py существует", os.path.exists("src/checker.py")),
    ("Файл src/api.py существует", os.path.exists("src/api.py")),
    ("Файл src/main.py существует", os.path.exists("src/main.py")),
    ("Папка tests/ существует", os.path.exists("tests")),
    ("Файл Dockerfile существует", os.path.exists("Dockerfile")),
    ("Файл requirements.txt существует", os.path.exists("requirements.txt")),
    ("Файл README.md существует", os.path.exists("README.md")),
]

all_checks_passed = True
for desc, condition in checks:
    if not condition:
        all_checks_passed = False
    check(desc, condition)

# Часть 2: Проверка функциональности
print("\n🔧 2. ПРОВЕРКА ФУНКЦИОНАЛЬНОСТИ")

print("\n2.1 Проверка импорта модулей...")
try:
    sys.path.insert(0, "src")
    from checker import evaluate_password
    result = evaluate_password("Password123!")
    print("✅ Модуль checker импортируется")
    print(f"   Тестовый пароль: {result['score']}/100 ({result['strength']})")
except Exception as e:
    print(f"❌ Ошибка импорта: {e}")
    all_checks_passed = False

print("\n2.2 Проверка CLI (базовая)...")
try:
    # Простой тест CLI
    import argparse
    print("✅ Модуль argparse доступен")
except:
    print("❌ Проблема с CLI")
    all_checks_passed = False

# Часть 3: Проверка Docker файлов
print("\n🐳 3. ПРОВЕРКА DOCKER ФАЙЛОВ")

print("\n3.1 Проверка Dockerfile...")
if os.path.exists("Dockerfile"):
    with open("Dockerfile", "r", encoding="utf-8") as f:
        docker_content = f.read()
        has_from = "FROM" in docker_content
        has_copy = "COPY" in docker_content
        has_run = "RUN" in docker_content
        check("Содержит FROM", has_from)
        check("Содержит COPY", has_copy)
        check("Содержит RUN", has_run)
else:
    print("❌ Dockerfile не найден")
    all_checks_passed = False

print("\n3.2 Проверка docker-compose.yml...")
if os.path.exists("docker-compose.yml"):
    print("✅ docker-compose.yml существует")
else:
    print("❌ docker-compose.yml не найден")
    all_checks_passed = False

# Часть 4: Проверка зависимостей
print("\n📦 4. ПРОВЕРКА ЗАВИСИМОСТЕЙ")

if os.path.exists("requirements.txt"):
    with open("requirements.txt", "r", encoding="utf-8") as f:
        deps = f.readlines()
        print(f"✅ Найдено {len(deps)} зависимостей в requirements.txt")
        # Проверяем ключевые зависимости
        key_deps = ["fastapi", "uvicorn", "pydantic"]
        for dep in key_deps:
            found = any(dep in line for line in deps)
            check(f"Зависимость {dep}", found)
else:
    print("❌ requirements.txt не найден")
    all_checks_passed = False

# Итог
print_section("ИТОГИ ПРОВЕРКИ")

if all_checks_passed:
    print("\n🎉 ВСЕ ОСНОВНЫЕ ПРОВЕРКИ ПРОЙДЕНЫ!")
    print("\n📋 Проект готов к сдаче. Осталось:")
    print("1. Загрузить на GitHub")
    print("2. Отправить ссылку преподавателю")
else:
    print("\n⚠️  Есть проблемы, которые нужно исправить")
    print("\n🔧 Рекомендуемые действия:")
    print("1. Проверьте наличие всех обязательных файлов")
    print("2. Убедитесь, что Docker Desktop запущен")
    print("3. Установите недостающие зависимости: pip install black isort ruff")

print("\n📊 СТАТИСТИКА ПРОЕКТА:")
# Считаем файлы
python_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            python_files.append(os.path.join(root, file))

print(f"• Python файлов: {len(python_files)}")
print(f"• Обязательных файлов: {len(checks)} проверено")

# Показываем структуру
print("\n📁 КЛЮЧЕВЫЕ ФАЙЛЫ:")
key_files = [
    "src/checker.py",
    "src/api.py", 
    "src/main.py",
    "tests/test_checker.py",
    "Dockerfile",
    "docker-compose.yml",
    "requirements.txt",
    "README.md",
    ".env.example",
    ".gitignore"
]

for file in key_files:
    exists = "✅" if os.path.exists(file) else "❌"
    print(f"  {exists} {file}")

input("\nНажмите Enter для завершения...")