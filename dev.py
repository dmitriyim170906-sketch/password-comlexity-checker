print("=" * 60)
print("PASSWORD CHECKER - ПРОСТОЙ ИНСТРУМЕНТ РАЗРАБОТКИ")
print("=" * 60)

def menu():
    while True:
        print("\nВЫБЕРИТЕ ДЕЙСТВИЕ:")
        print("1. Проверить, что Python работает")
        print("2. Проверить основные импорты")
        print("3. Запустить простой тест пароля")
        print("4. Запустить API сервер")
        print("5. Проверить структуру проекта")
        print("6. Выход")
        
        choice = input("\nВаш выбор (1-6): ")
        
        if choice == "1":
            check_python()
        elif choice == "2":
            check_imports()
        elif choice == "3":
            test_password()
        elif choice == "4":
            run_api()
        elif choice == "5":
            check_project()
        elif choice == "6":
            print("Выход...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

def check_python():
    """Проверяем, что Python работает"""
    print("\n[1] ПРОВЕРКА PYTHON")
    print("-" * 40)
    
    import sys
    import os
    
    print(f"Версия Python: {sys.version}")
    print(f"Папка проекта: {os.getcwd()}")
    print(f"Python находится: {sys.executable}")
    
    # Проверяем venv
    if "venv" in sys.executable or "virtualenv" in sys.executable:
        print("✅ Виртуальное окружение активировано")
    else:
        print("⚠️  Виртуальное окружение НЕ активировано")
        print("   Выполните: venv\\Scripts\\activate")
    
    input("\nНажмите Enter чтобы продолжить...")

def check_imports():
    """Проверяем основные импорты"""
    print("\n[2] ПРОВЕРКА ИМПОРТОВ")
    print("-" * 40)
    
    imports_to_check = [
        ("checker", "from checker import evaluate_password"),
        ("config", "from config import config"),
        ("fastapi", "import fastapi"),
        ("uvicorn", "import uvicorn"),
    ]
    
    for module_name, import_cmd in imports_to_check:
        try:
            # Создаем временный код для импорта
            code = f"""
try:
    {import_cmd}
    print("✅ {module_name} - импортируется успешно")
except Exception as e:
    print(f"❌ {{module_name}} - ошибка: {{e}}")
"""
            exec(code)
        except Exception as e:
            print(f"❌ {module_name} - критическая ошибка: {e}")
    
    input("\nНажмите Enter чтобы продолжить...")

def test_password():
    """Тестируем проверку пароля"""
    print("\n[3] ТЕСТ ПРОВЕРКИ ПАРОЛЯ")
    print("-" * 40)
    
    try:
        # Прямой импорт с добавлением пути
        import sys
        import os
        sys.path.insert(0, os.path.join(os.getcwd(), 'src'))
        
        from checker import evaluate_password
        
        test_passwords = [
            "123",
            "password",
            "Password123",
            "P@ssw0rd!",
            "MySuper$tr0ngP@ss2024!"
        ]
        
        for pwd in test_passwords:
            result = evaluate_password(pwd)
            print(f"\nПароль: '{pwd}'")
            print(f"  Балл: {result['score']}/100")
            print(f"  Уровень: {result['strength']}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        print("Совет: Убедитесь, что файл src/checker.py существует")
    
    input("\nНажмите Enter чтобы продолжить...")

def run_api():
    """Запускаем API сервер"""
    print("\n[4] ЗАПУСК API СЕРВЕРА")
    print("-" * 40)
    
    print("Это запустит API сервер на http://localhost:8000")
    print("После запуска откройте в браузере: http://localhost:8000/docs")
    print("Для остановки нажмите Ctrl+C")
    print("\nЗапустить? (y/n): ", end="")
    
    if input().lower() != 'y':
        return
    
    try:
        import uvicorn
        import sys
        import os
        
        # Добавляем src в путь
        sys.path.insert(0, os.path.join(os.getcwd(), 'src'))
        
        print("\nЗапускаем API...")
        print("Откройте: http://localhost:8000/docs")
        print("=" * 40)
        
        uvicorn.run(
            "api:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
        
    except Exception as e:
        print(f"❌ Ошибка при запуске API: {e}")
        input("\nНажмите Enter чтобы продолжить...")

def check_project():
    """Проверяем структуру проекта"""
    print("\n[5] ПРОВЕРКА СТРУКТУРЫ ПРОЕКТА")
    print("-" * 40)
    
    import os
    
    required_files = [
        ("src/", "папка с кодом"),
        ("src/checker.py", "модуль проверки паролей"),
        ("src/api.py", "API сервер"),
        ("src/main.py", "CLI интерфейс"),
        ("requirements.txt", "зависимости"),
        ("Dockerfile", "конфигурация Docker"),
        ("docker-compose.yml", "docker-compose"),
    ]
    
    print("Проверяем файлы проекта:")
    for file_path, description in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} - {description}")
        else:
            print(f"❌ {file_path} - НЕ НАЙДЕН ({description})")
    
    # Показываем дерево проекта
    print("\nСодержимое папки проекта:")
    for item in os.listdir("."):
        if os.path.isdir(item):
            print(f"📁 {item}/")
        else:
            print(f"📄 {item}")
    
    input("\nНажмите Enter чтобы продолжить...")

if __name__ == "__main__":
    menu()