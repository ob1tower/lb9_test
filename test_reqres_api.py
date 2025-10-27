import requests

API_BASE = "https://reqres.in/api"
TIMEOUT_SEC = 10
HEADERS = {"Content-Type": "application/json", "x-api-key": "reqres-free-v1"}

class TestAPI:
    """
    Класс тестов для работы с REST API!
    """
    def test_get_single_user(self):
        """
        Проверка получения информации о пользователе
        """
        resp = requests.get(f"{API_BASE}/users/1", headers=HEADERS, timeout=TIMEOUT_SEC)
        assert resp.status_code == 200, "Код ответа не 200"

        result = resp.json()
        assert "data" in result, "В ответе отсутствуют данные"
        user = result["data"]
        required_fields = ["id", "email", "first_name", "last_name", "avatar"]
        for field in required_fields:
            assert field in user, f"Отсутствует поле {field}"
        
        assert user["id"] == 1, "Неверный ID пользователя"
        assert "@" in user["email"], "Некорректный email"

    def test_add_user(self):
        """
        Проверка создания нового пользователя!
        """
        user_data = {
            "fullName": "Elizaveta Vladimirova",
            "position": "Backend Developer",
            "years": 23
        }
        resp = requests.post(f"{API_BASE}/users", json=user_data, headers=HEADERS, timeout=TIMEOUT_SEC)
        assert resp.status_code == 201, "Код ответа не 201"

        result = resp.json()
        expected_keys = ["fullName", "position", "years", "id", "createdAt"]
        for key in expected_keys:
            assert key in result, f"В ответе отсутствует поле {key}"
        
        assert result["fullName"] == "Elizaveta Vladimirova", "Имя не совпадает"
        assert result["position"] == "Backend Developer", "Должность не совпадает"
        assert result["years"] == 23, "Возраст не совпадает"

    def test_modify_user(self):
        """
        Проверка обновления данных пользователя
        """
        update_data = {
            "fullName": "Elizaveta Vladimirova",
            "position": "Data Scientist",
            "years": 24
        }
        resp = requests.put(f"{API_BASE}/users/2", json=update_data, headers=HEADERS, timeout=TIMEOUT_SEC)
        assert resp.status_code == 200, "Код ответа не 200"

        result = resp.json()
        expected_keys = ["fullName", "position", "years", "updatedAt"]
        for key in expected_keys:
            assert key in result, f"В ответе отсутствует поле {key}"

        assert result["fullName"] == "Elizaveta Vladimirova", "Имя не совпадает"
        assert result["position"] == "Data Scientist", "Должность не совпадает"
        assert result["years"] == 24, "Возраст не совпадает"
