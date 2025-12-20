"""
Web API для проверки паролей.
Позволяет проверять пароли через HTTP-запросы.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from checker import evaluate_password
from config import config


# Создаем FastAPI приложение
app = FastAPI(
    title="Password Complexity Checker API",
    description="API для проверки сложности паролей",
    version="1.0.0",
)


# Модель для запроса
class PasswordRequest(BaseModel):
    """Модель запроса для проверки пароля."""
    password: str


# Модель для ответа
class CheckResult(BaseModel):
    """Модель результата проверки."""
    password: str
    score: int
    max_score: int
    strength: str
    details: List[dict]


# Модель для массовой проверки
class BatchRequest(BaseModel):
    """Модель для массовой проверки паролей."""
    passwords: List[str]


# Модель для ответа с несколькими результатами
class BatchResult(BaseModel):
    """Результат массовой проверки."""
    results: List[CheckResult]
    total_count: int
    strong_count: int
    weak_count: int


@app.get("/")
async def root():
    """Корневой эндпоинт - информация о API."""
    return {
        "service": "Password Complexity Checker",
        "version": "1.0.0",
        "endpoints": {
            "GET /": "Эта информация",
            "POST /check": "Проверить один пароль",
            "POST /check/batch": "Проверить несколько паролей",
            "GET /config": "Показать текущую конфигурацию",
            "GET /health": "Проверить работоспособность сервиса",
        },
        "documentation": "/docs или /redoc"
    }


@app.post("/check", response_model=CheckResult)
async def check_password(request: PasswordRequest):
    """
    Проверяет сложность одного пароля.
    
    Args:
        request: Объект с паролем для проверки
        
    Returns:
        Результат проверки пароля
    """
    try:
        result = evaluate_password(request.password)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при проверке пароля: {str(e)}")


@app.post("/check/batch", response_model=BatchResult)
async def check_passwords_batch(request: BatchRequest):
    """
    Проверяет несколько паролей за один запрос.
    
    Args:
        request: Объект со списком паролей
        
    Returns:
        Результаты проверки всех паролей
    """
    try:
        results = [evaluate_password(pwd) for pwd in request.passwords]
        
        # Считаем статистику
        strong_passwords = sum(1 for r in results if r["score"] >= 70)
        weak_passwords = sum(1 for r in results if r["score"] < 50)
        
        return {
            "results": results,
            "total_count": len(results),
            "strong_count": strong_passwords,
            "weak_count": weak_passwords,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при массовой проверке: {str(e)}")


@app.get("/config")
async def get_config():
    """Возвращает текущую конфигурацию приложения."""
    return {
        "config": config,
        "password_rules": {
            "min_length": config["min_password_length"],
            "require_digits": config["require_digits"],
            "require_uppercase": config["require_uppercase"],
            "require_lowercase": config["require_lowercase"],
            "require_special": config["require_special_chars"],
        }
    }


@app.get("/health")
async def health_check():
    """Проверяет работоспособность сервиса."""
    return {
        "status": "healthy",
        "service": "password-checker",
        "timestamp": "2024-01-01T12:00:00Z"  # В реальном приложении здесь будет datetime.now()
    }


# Если файл запущен напрямую (для тестирования)
if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Запускаем Password Checker API...")
    print(f"📡 Адрес: http://{config['api_host']}:{config['api_port']}")
    print(f"📖 Документация: http://{config['api_host']}:{config['api_port']}/docs")
    print("⚙️ Конфигурация:")
    for key, value in config.items():
        print(f"  {key}: {value}")
    
    uvicorn.run(
        app,
        host=config["api_host"],
        port=config["api_port"],
        log_level=config["log_level"].lower()
    )