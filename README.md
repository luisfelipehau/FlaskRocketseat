# Flask Task API

## Descrição
Este é um projeto de exemplo de uma API simples de tarefas (tasks) usando Flask. A API permite a criação, leitura, atualização e exclusão de tarefas.

Projeto do curso de Python da Rocketseat (Módulo 3 - Flask)

## Pré-requisitos
- Python 3.x
- Flask
- pytest
- requests

## Instalação
1. Clone o repositório para o seu ambiente local:

    ```
    git clone https://github.com/luisfelipehau/FlaskRocketseat.git
    ```

2. Instale as dependências do projeto:

    ```
    pip install -r requirements.txt
    ```

## Uso
1. Inicie o servidor Flask executando o arquivo `app.py`:

    ```
    python app.py
    ```

2. Execute os testes automatizados usando o pytest:

    ```
    python -m pytest tests.py -v
    ```

## Endpoints
- `POST /tasks`: Cria uma nova tarefa.
- `GET /tasks`: Retorna todas as tarefas.
- `GET /tasks/<id>`: Retorna uma tarefa específica pelo ID.
- `PUT /tasks/<id>`: Atualiza uma tarefa existente pelo ID.
- `DELETE /tasks/<id>`: Exclui uma tarefa pelo ID.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

