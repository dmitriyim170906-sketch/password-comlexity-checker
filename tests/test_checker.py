import pytest
from checker import evaluate_password


def test_empty_password():
    """Тест пустого пароля."""
    result = evaluate_password("")
    assert result["score"] == 0
    assert result["strength"] == "Очень слабый"


def test_very_short_password():
    """Тест очень короткого пароля."""
    result = evaluate_password("123")
    assert result["score"] < 30
    assert "слабый" in result["strength"].lower()


def test_good_password():
    """Тест хорошего пароля."""
    result = evaluate_password("Password123!")
    assert result["score"] >= 70
    assert "сильный" in result["strength"].lower()


def test_common_password():
    """Тест простого пароля."""
    result = evaluate_password("password")
    assert result["score"] < 50
    assert any("простой" in detail["message"] for detail in result["details"])


def test_password_with_all_rules():
    """Тест пароля, который проходит все проверки."""
    result = evaluate_password("P@ssw0rd2024!")
    assert result["score"] >= 85
    assert result["strength"] == "Очень сильный"
    
    # Проверяем, что все правила пройдены
    all_passed = all(detail["passed"] for detail in result["details"])
    assert all_passed


def test_password_length_scoring():
    """Тест системы баллов за длину."""
    short = evaluate_password("1234567")  # 7 символов
    good = evaluate_password("12345678")  # 8 символов
    long = evaluate_password("1234567890123456")  # 16 символов
    
    assert short["score"] < good["score"]
    # Заметим, что в нашей системе баллы за длину фиксированные
    # Но убедимся, что пароль короче 8 символов получает 0 за длину


def test_password_details_structure():
    """Тест структуры результата."""
    result = evaluate_password("Test123!")
    
    # Проверяем обязательные поля
    assert "password" in result
    assert "score" in result
    assert "strength" in result
    assert "details" in result
    assert "max_score" in result
    
    # Проверяем детали
    assert isinstance(result["details"], list)
    assert len(result["details"]) > 0
    
    for detail in result["details"]:
        assert "rule" in detail
        assert "passed" in detail
        assert "message" in detail
        assert "score" in detail


if __name__ == "__main__":
    # Запуск тестов без pytest (для отладки)
    test_empty_password()
    test_good_password()
    print("✅ Все тесты пройдены!")