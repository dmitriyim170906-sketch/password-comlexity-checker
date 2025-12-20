"""
CLI (Command Line Interface) для проверки паролей.
Позволяет проверять пароли прямо из командной строки.
"""

import argparse
import json
from typing import Optional
from checker import evaluate_password
from config import config


def check_single_password(password: str, json_output: bool = False):
    """
    Проверяет один пароль и выводит результат.
    
    Args:
        password (str): Пароль для проверки
        json_output (bool): Выводить результат в формате JSON
    """
    result = evaluate_password(password)
    
    if json_output:
        # Вывод в формате JSON (удобно для автоматической обработки)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        # Красивый вывод для человека
        print("\n" + "=" * 50)
        print(f"🔐 РЕЗУЛЬТАТ ПРОВЕРКИ ПАРОЛЯ")
        print("=" * 50)
        print(f"Пароль: {result['password']}")
        print(f"Общий балл: {result['score']}/{result['max_score']}")
        print(f"Уровень сложности: {result['strength']}")
        print("\n📋 Детали проверки:")
        
        for detail in result["details"]:
            status = "✅ ПРОЙДЕНО" if detail["passed"] else "❌ НЕ ПРОЙДЕНО"
            print(f"  {status}")
            print(f"    Правило: {detail['rule']}")
            print(f"    Сообщение: {detail['message']}")
            print(f"    Баллы: {detail['score']}")
            print()
        
        print("=" * 50)


def check_from_file(filename: str, json_output: bool = False):
    """
    Читает пароли из файла и проверяет их.
    
    Args:
        filename (str): Имя файла с паролями
        json_output (bool): Выводить результат в формате JSON
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            passwords = [line.strip() for line in file if line.strip()]
        
        if json_output:
            results = [evaluate_password(pwd) for pwd in passwords]
            print(json.dumps(results, ensure_ascii=False, indent=2))
        else:
            print(f"\n📁 Проверяем пароли из файла: {filename}")
            print(f"Найдено паролей: {len(passwords)}")
            print("=" * 50)
            
            for i, password in enumerate(passwords, 1):
                result = evaluate_password(password)
                print(f"{i}. '{password}' - {result['score']}/100 ({result['strength']})")
            
            print("=" * 50)
            
    except FileNotFoundError:
        print(f"❌ Ошибка: Файл '{filename}' не найден!")
    except Exception as e:
        print(f"❌ Ошибка при чтении файла: {e}")


def create_sample_file():
    """Создает пример файла с паролями для тестирования."""
    sample_passwords = [
        "123456",
        "password",
        "Password123",
        "P@ssw0rd!",
        "MySuper$tr0ngP@ss!",
        "qwerty",
        "admin123",
        "Welcome2024!",
    ]
    
    with open("sample_passwords.txt", "w", encoding='utf-8') as file:
        for pwd in sample_passwords:
            file.write(pwd + "\n")
    
    print("✅ Создан файл sample_passwords.txt с тестовыми паролями")
    print("Используйте: python src/main.py --file sample_passwords.txt")


def main():
    """Основная функция CLI."""
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(
        description="Проверка сложности паролей",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python src/main.py --password "MyPass123!"
  python src/main.py --password "test" --json
  python src/main.py --file passwords.txt
  python src/main.py --create-sample
        """
    )
    
    # Добавляем аргументы
    parser.add_argument(
        "-p", "--password",
        help="Проверить один пароль"
    )
    
    parser.add_argument(
        "-f", "--file",
        help="Проверить пароли из файла"
    )
    
    parser.add_argument(
        "-j", "--json",
        action="store_true",
        help="Вывести результат в формате JSON"
    )
    
    parser.add_argument(
        "--create-sample",
        action="store_true",
        help="Создать пример файла с паролями"
    )
    
    parser.add_argument(
        "--show-config",
        action="store_true",
        help="Показать текущую конфигурацию"
    )
    
    # Парсим аргументы
    args = parser.parse_args()
    
    # Обрабатываем аргументы
    if args.show_config:
        from config import print_config
        print_config()
    
    elif args.create_sample:
        create_sample_file()
    
    elif args.password:
        check_single_password(args.password, args.json)
    
    elif args.file:
        check_from_file(args.file, args.json)
    
    else:
        # Если не указаны аргументы - показываем справку
        parser.print_help()
        
        # Дополнительно предлагаем интерактивный режим
        print("\n🎮 ИНТЕРАКТИВНЫЙ РЕЖИМ")
        print("Хотите проверить пароль в интерактивном режиме? (y/n)")
        
        choice = input().lower()
        if choice == 'y':
            password = input("Введите пароль для проверки: ")
            check_single_password(password)


if __name__ == "__main__":
    main()