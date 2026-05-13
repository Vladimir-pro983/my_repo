import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import requests  # noqa: E402
import pytest  # noqa: E402
from config import BASE_URL, HEADERS  # noqa: E402


# ========== ПОЗИТИВНЫЕ ТЕСТЫ ==========

def test_create_project_positive():
    """Позитивный тест: создание проекта."""
    payload = {"title": "Новый проект"}
    response = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json=payload
    )

    assert response.status_code == 201
    data = response.json()
    assert "id" in data

    # Проверяем title через GET-запрос
    project_id = data["id"]
    get_response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS
    )
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Новый проект"

    # Cleanup: удаляем проект после теста
    if project_id:
        requests.delete(
            f"{BASE_URL}/projects/{project_id}",
            headers=HEADERS
        )


def test_get_project_positive():
    """Позитивный тест: получение проекта."""
    # Создаём проект для теста
    payload = {"title": "Тестовый проект"}
    create_response = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json=payload
    )
    project_id = create_response.json()["id"]

    # Получаем проект
    response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS
    )

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Тестовый проект"

    # Cleanup: удаляем проект
    requests.delete(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS
    )


@pytest.fixture
def create_project():
    """Фикстура для создания и удаления проекта."""
    created_ids = []

    def _create(title):
        payload = {"title": title}
        response = requests.post(
            f"{BASE_URL}/projects",
            headers=HEADERS,
            json=payload
        )
        project_id = response.json().get("id")
        created_ids.append(project_id)
        return project_id

    yield _create

    # Cleanup: удаляем все созданные проекты
    for project_id in created_ids:
        if project_id:
            requests.delete(
                f"{BASE_URL}/projects/{project_id}",
                headers=HEADERS
            )


def test_update_project_positive(create_project):
    """Позитивный тест: обновление проекта."""
    project_id = create_project("Старое название")

    payload = {"title": "Новое название"}
    response = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS,
        json=payload
    )

    assert response.status_code == 200

    # Проверяем обновление через GET-запрос
    get_response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS
    )
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Новое название"


# ========== НЕГАТИВНЫЕ ТЕСТЫ ==========

def test_create_project_negative_no_title():
    """Негативный тест: создание проекта без обязательного поля title."""
    payload = {}
    response = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json=payload
    )

    assert response.status_code == 400


def test_get_project_negative_invalid_id():
    """Негативный тест: получение проекта с несуществующим ID."""
    response = requests.get(
        f"{BASE_URL}/projects/invalid_id_12345",
        headers=HEADERS
    )

    assert response.status_code == 404


def test_update_project_negative_invalid_id():
    """Негативный тест: обновление проекта с несуществующим ID."""
    payload = {"title": "Новое название"}
    response = requests.put(
        f"{BASE_URL}/projects/invalid_id_12345",
        headers=HEADERS,
        json=payload
    )

    assert response.status_code == 404
