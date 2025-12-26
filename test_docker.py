<<<<<<< HEAD
"""
Простой скрипт для тестирования API.
Можно запустить после запуска Docker-контейнера.
"""

import requests
import json

def test_api():
    """Тестирует основные эндпоинты API."""
    
    base_url = "http://localhost:8000"
    
    print("🔍 Тестируем Password Checker API")
    print("=" * 50)
    
    try:
        # 1. Проверяем корневой эндпоинт
        print("1. Проверяем корневой эндпоинт...")
        response = requests.get(f"{base_url}/")
        print(f"   ✅ Ответ: {response.json()['service']}")
        
        # 2. Проверяем health check
        print("\n2. Проверяем health check...")
        response = requests.get(f"{base_url}/health")
        print(f"   ✅ Статус: {response.json()['status']}")
        
        # 3. Проверяем конфигурацию
        print("\n3. Проверяем конфигурацию...")
        response = requests.get(f"{base_url}/config")
        config = response.json()
        print(f"   ✅ Минимальная длина пароля: {config['password_rules']['min_length']}")
        
        # 4. Проверяем один пароль
        print("\n4. Проверяем пароль '123'...")
        response = requests.post(
            f"{base_url}/check",
            json={"password": "123"}
        )
        result = response.json()
        print(f"   ✅ Результат: {result['score']}/100 ({result['strength']})")
        
        # 5. Проверяем хороший пароль
        print("\n5. Проверяем пароль 'P@ssw0rd!'...")
        response = requests.post(
            f"{base_url}/check",
            json={"password": "P@ssw0rd!"}
        )
        result = response.json()
        print(f"   ✅ Результат: {result['score']}/100 ({result['strength']})")
        
        # 6. Массовая проверка
        print("\n6. Проверяем несколько паролей...")
        response = requests.post(
            f"{base_url}/check/batch",
            json={"passwords": ["123", "password", "P@ssw0rd!"]}
        )
        result = response.json()
        print(f"   ✅ Проверено: {result['total_count']} паролей")
        print(f"   ✅ Сильных: {result['strong_count']}, Слабых: {result['weak_count']}")
        
        print("\n" + "=" * 50)
        print("🎉 Все тесты пройдены успешно!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Ошибка: Не удалось подключиться к API")
        print("   Убедитесь, что контейнер запущен: docker-compose up")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    test_api()
=======
"""
Простой скрипт для тестирования API.
Можно запустить после запуска Docker-контейнера.
"""

import requests
import json

def test_api():
    """Тестирует основные эндпоинты API."""
    
    base_url = "http://localhost:8000"
    
    print("🔍 Тестируем Password Checker API")
    print("=" * 50)
    
    try:
        # 1. Проверяем корневой эндпоинт
        print("1. Проверяем корневой эндпоинт...")
        response = requests.get(f"{base_url}/")
        print(f"   ✅ Ответ: {response.json()['service']}")
        
        # 2. Проверяем health check
        print("\n2. Проверяем health check...")
        response = requests.get(f"{base_url}/health")
        print(f"   ✅ Статус: {response.json()['status']}")
        
        # 3. Проверяем конфигурацию
        print("\n3. Проверяем конфигурацию...")
        response = requests.get(f"{base_url}/config")
        config = response.json()
        print(f"   ✅ Минимальная длина пароля: {config['password_rules']['min_length']}")
        
        # 4. Проверяем один пароль
        print("\n4. Проверяем пароль '123'...")
        response = requests.post(
            f"{base_url}/check",
            json={"password": "123"}
        )
        result = response.json()
        print(f"   ✅ Результат: {result['score']}/100 ({result['strength']})")
        
        # 5. Проверяем хороший пароль
        print("\n5. Проверяем пароль 'P@ssw0rd!'...")
        response = requests.post(
            f"{base_url}/check",
            json={"password": "P@ssw0rd!"}
        )
        result = response.json()
        print(f"   ✅ Результат: {result['score']}/100 ({result['strength']})")
        
        # 6. Массовая проверка
        print("\n6. Проверяем несколько паролей...")
        response = requests.post(
            f"{base_url}/check/batch",
            json={"passwords": ["123", "password", "P@ssw0rd!"]}
        )
        result = response.json()
        print(f"   ✅ Проверено: {result['total_count']} паролей")
        print(f"   ✅ Сильных: {result['strong_count']}, Слабых: {result['weak_count']}")
        
        print("\n" + "=" * 50)
        print("🎉 Все тесты пройдены успешно!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Ошибка: Не удалось подключиться к API")
        print("   Убедитесь, что контейнер запущен: docker-compose up")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    test_api()
>>>>>>> 4ce59620b51de28efa36a518268458c4bfcab2ec
