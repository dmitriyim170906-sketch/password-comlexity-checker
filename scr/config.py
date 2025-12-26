import os
from typing import Dict, Any


def load_config() -> Dict[str, Any]:
    """
    Загружает конфигурацию приложения.
    
    Returns:
        Dict[str, Any]: Словарь с настройками
    """
    return {
        # Настройки проверки паролей
        "min_password_length": int(os.getenv("MIN_PASSWORD_LENGTH", "8")),
        "require_digits": os.getenv("REQUIRE_DIGITS", "true").lower() == "true",
        "require_uppercase": os.getenv("REQUIRE_UPPERCASE", "true").lower() == "true",
        "require_lowercase": os.getenv("REQUIRE_LOWERCASE", "true").lower() == "true",
        "require_special_chars": os.getenv("REQUIRE_SPECIAL_CHARS", "true").lower() == "true",
        
        # Настройки приложения
        "debug": os.getenv("DEBUG", "false").lower() == "true",
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        
        # Настройки API
        "api_host": os.getenv("API_HOST", "0.0.0.0"),
        "api_port": int(os.getenv("API_PORT", "8000")),
    }


# Создаем глобальный объект конфигурации
config = load_config()


def print_config():
    """Выводит текущую конфигурацию (для отладки)."""
    print("⚙️ ТЕКУЩАЯ КОНФИГУРАЦИЯ:")
    print("=" * 30)
    for key, value in config.items():
        print(f"  {key}: {value}")
    print("=" * 30)


# Если файл запущен напрямую - показываем конфигурацию
if __name__ == "__main__":
    print_config()
