"""
Тесты для API (требует запущенного сервера).
"""

import pytest
import requests


@pytest.fixture
def api_url():
    """Базовый URL API."""
    return "http://localhost:8000"


def test_api_health(api_url):
    """Тест health check эндпоинта."""
    response = requests.get(f"{api_url}/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_api_root(api_url):
    """Тест корневого эндпоинта."""
    response = requests.get(api_url)
    assert response.status_code == 200
    data = response.json()
    assert "service" in data
    assert "version" in data


def test_api_check_password(api_url):
    """Тест проверки пароля через API."""
    response = requests.post(
        f"{api_url}/check",
        json={"password": "Test123!"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "score" in data
    assert "strength" in data
    assert "details" in data


def test_api_batch_check(api_url):
    """Тест массовой проверки паролей."""
    response = requests.post(
        f"{api_url}/check/batch",
        json={"passwords": ["123", "password", "P@ssw0rd!"]}
    )
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert "total_count" in data
    assert len(data["results"]) == 3


def test_api_config(api_url):
    """Тест эндпоинта конфигурации."""
    response = requests.get(f"{api_url}/config")
    assert response.status_code == 200
    data = response.json()
    assert "config" in data
    assert "password_rules" in data


def test_api_invalid_json(api_url):
    """Тест обработки невалидного JSON."""
    response = requests.post(
        f"{api_url}/check",
        data="invalid json",
        headers={"Content-Type": "application/json"}
    )
    # FastAPI должен вернуть 422 за невалидный JSON
    assert response.status_code == 422


if __name__ == "__main__":
    # Быстрый тест без pytest
    print("⚠️  Запустите сервер перед тестированием: docker-compose up -d")
    print("URL: http://localhost:8000")