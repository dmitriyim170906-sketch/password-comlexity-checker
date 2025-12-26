def check_length(password: str, min_length: int = 8) -> dict:
    """
    Проверяет длину пароля.
    
    Args:
        password (str): Пароль для проверки
        min_length (int): Минимальная требуемая длина
        
    Returns:
        dict: Результат проверки
    """
    is_valid = len(password) >= min_length
    
    return {
        "rule": "Минимальная длина",
        "passed": is_valid,
        "message": f"Длина: {len(password)} символов (минимум {min_length})",
        "score": 20 if is_valid else 0  # 20 баллов за длину
    }


def check_digits(password: str) -> dict:
    """
    Проверяет наличие цифр в пароле.
    
    Args:
        password (str): Пароль для проверки
        
    Returns:
        dict: Результат проверки
    """
    has_digits = any(char.isdigit() for char in password)
    
    return {
        "rule": "Наличие цифр",
        "passed": has_digits,
        "message": "Есть цифры" if has_digits else "Нет цифр",
        "score": 15 if has_digits else 0  # 15 баллов за цифры
    }


def check_uppercase(password: str) -> dict:
    """
    Проверяет наличие заглавных букв.
    
    Args:
        password (str): Пароль для проверки
        
    Returns:
        dict: Результат проверки
    """
    has_upper = any(char.isupper() for char in password)
    
    return {
        "rule": "Заглавные буквы",
        "passed": has_upper,
        "message": "Есть заглавные буквы" if has_upper else "Нет заглавных букв",
        "score": 15 if has_upper else 0
    }


def check_lowercase(password: str) -> dict:
    """
    Проверяет наличие строчных букв.
    
    Args:
        password (str): Пароль для проверки
        
    Returns:
        dict: Результат проверки
    """
    has_lower = any(char.islower() for char in password)
    
    return {
        "rule": "Строчные буквы",
        "passed": has_lower,
        "message": "Есть строчные буквы" if has_lower else "Нет строчных букв",
        "score": 15 if has_lower else 0
    }


def check_special_chars(password: str) -> dict:
    """
    Проверяет наличие специальных символов.
    
    Args:
        password (str): Пароль для проверки
        
    Returns:
        dict: Результат проверки
    """
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?`~"
    has_special = any(char in special_chars for char in password)
    
    return {
        "rule": "Специальные символы",
        "passed": has_special,
        "message": "Есть спецсимволы" if has_special else "Нет спецсимволов",
        "score": 20 if has_special else 0
    }


def check_common_passwords(password: str) -> dict:
    """
    Проверяет, не является ли пароль слишком простым.
    
    Args:
        password (str): Пароль для проверки
        
    Returns:
        dict: Результат проверки
    """
    common_passwords = [
        "123456", "password", "12345678", "qwerty", "123456789",
        "12345", "1234", "111111", "1234567", "dragon",
        "123123", "baseball", "abc123", "football", "monkey",
        "letmein", "shadow", "master", "666666", "qwertyuiop"
    ]
    
    is_common = password.lower() in common_passwords
    
    return {
        "rule": "Не слишком простой",
        "passed": not is_common,
        "message": "Не является простым паролем" if not is_common else "Слишком простой пароль!",
        "score": 15 if not is_common else 0
    }


# ==========================================
# ГЛАВНАЯ ФУНКЦИЯ - СБИРАЕМ ВСЕ ДЕТАЛИ ВМЕСТЕ
# ==========================================

def evaluate_password(password: str) -> dict:
    """
    Основная функция для оценки пароля.
    Собирает все проверки вместе и выдает итоговый результат.
    
    Args:
        password (str): Пароль для проверки
        
    Returns:
        dict: Полный результат проверки
    """
    if not password:
        return {
            "password": "",
            "score": 0,
            "strength": "Очень слабый",
            "details": [{
                "rule": "Пустой пароль",
                "passed": False,
                "message": "Пароль не может быть пустым",
                "score": 0
            }]
        }
    
    # Выполняем все проверки
    checks = [
        check_length(password),
        check_digits(password),
        check_uppercase(password),
        check_lowercase(password),
        check_special_chars(password),
        check_common_passwords(password),
    ]
    
    # Считаем общий балл
    total_score = sum(check["score"] for check in checks)
    
    # Определяем уровень сложности
    if total_score >= 90:
        strength = "Очень сильный"
    elif total_score >= 70:
        strength = "Сильный"
    elif total_score >= 50:
        strength = "Средний"
    elif total_score >= 30:
        strength = "Слабый"
    else:
        strength = "Очень слабый"
    
    # Возвращаем полный результат
    return {
        "password": password,
        "score": total_score,
        "strength": strength,
        "max_score": 100,
        "details": checks
    }


# ==========================================
# ТЕСТИРОВАНИЕ - проверяем, что все работает
# ==========================================

if __name__ == "__main__":
    print("ТЕСТИРУЕМ ПРОВЕРКУ ПАРОЛЕЙ")
    print("=" * 40)
    
    # Тестовые пароли
    test_passwords = [
        "",                    # Пустой
        "123",                # Очень короткий
        "password",           # Простой, только буквы
        "Password123",        # Без спецсимволов
        "P@ssw0rd!",         # Хороший пароль
        "MySuper$tr0ngP@ss!", # Отличный пароль
    ]
    
    for pwd in test_passwords:
        print(f"\n Проверяем пароль: '{pwd}'")
        result = evaluate_password(pwd)
        
        print(f"   Балл: {result['score']}/100")
        print(f"   Уровень: {result['strength']}")
        
        # Показываем детали
        print("   Детали проверки:")
        for detail in result["details"]:
            status = "✅" if detail["passed"] else "❌"
            print(f"     {status} {detail['rule']}: {detail['message']}")
    
    print("\n" + "=" * 40)
    print(" Проверка завершена!")
