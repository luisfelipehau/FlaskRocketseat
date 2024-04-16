from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete = Criar, Ler, Atualizar, Deletar
# Tabela: Tarefa

# Lista de tarefas
tasks = []
# Controle de ID para novas tarefas
task_id_control = 1


@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control
    # Recebe os dados da nova tarefa em formato JSON
    data = request.get_json()
    # Cria uma nova instância de Task com os dados fornecidos
    new_task = Task(
        id=task_id_control, title=data["title"], description=data.get("description", "")
    )
    # Incrementa o ID para a próxima tarefa
    task_id_control += 1
    # Adiciona a nova tarefa à lista de tarefas
    tasks.append(new_task)
    print(tasks)  # Debugging: imprime a lista de tarefas
    return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    # Converte a lista de tarefas em uma lista de dicionários
    task_list = [task.to_dict() for task in tasks]
    # Cria um dicionário de saída com a lista de tarefas e o total de tarefas
    output = {"tasks": task_list, "total_tasks": len(task_list)}
    return jsonify(output)


@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    # Procura a tarefa com o ID fornecido
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    # Retorna uma mensagem de erro se a tarefa não for encontrada
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = None
    # Procura a tarefa com o ID fornecido
    for t in tasks:
        if t.id == id:
            task = t
            break

    # Retorna uma mensagem de erro se a tarefa não for encontrada
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    # Atualiza os dados da tarefa com os novos dados fornecidos
    data = request.get_json()
    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]
    return jsonify({"message": "Tarefa atualizada com sucesso"})


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = None
    # Procura a tarefa com o ID fornecido
    for t in tasks:
        if t.id == id:
            task = t
            break
    # Retorna uma mensagem de erro se a tarefa não for encontrada
    if not task:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    # Remove a tarefa da lista de tarefas
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)
