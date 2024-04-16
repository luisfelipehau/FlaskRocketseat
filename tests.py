import pytest
import requests

# CRUD
BASE_URL = "http://127.0.0.1:5000"
tasks = []


def test_create_task():
    # Testa a criação de uma nova tarefa
    new_task_data = {"title": "Nova tarefa", "description": "Descrição da nova tarefa"}
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    # Verifica se a resposta foi bem-sucedida (status code 200)
    assert response.status_code == 200
    response_json = response.json()
    # Verifica se a resposta contém a mensagem e o ID da nova tarefa
    assert "message" in response_json
    assert "id" in response_json
    # Adiciona o ID da nova tarefa à lista de tarefas para uso nos outros testes
    tasks.append(response_json["id"])


def test_get_tasks():
    # Testa a obtenção da lista de tarefas
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    # Verifica se a resposta contém a lista de tarefas e o total de tarefas
    assert "tasks" in response_json
    assert "total_tasks" in response_json


def test_get_task():
    # Testa a obtenção de uma tarefa específica
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        # Verifica se o ID da tarefa retornada é o mesmo da tarefa criada anteriormente
        assert task_id == response_json["id"]


def test_update_task():
    # Testa a atualização de uma tarefa existente
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": True,
            "description": "Nova descrição",
            "title": "Título atualizado",
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        assert response.status_code == 200
        response_json = response.json()
        # Verifica se a resposta contém a mensagem de sucesso
        assert "message" in response_json

        # Verifica se os dados da tarefa foram atualizados corretamente
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == payload["title"]
        assert response_json["description"] == payload["description"]
        assert response_json["completed"] == payload["completed"]


def test_delete_task():
    # Testa a exclusão de uma tarefa
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200

        # Verifica se a tarefa foi excluída corretamente
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404
