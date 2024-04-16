class Task:
    def __init__(self, id, title, description, completed=False) -> None:
        """
        Inicializa uma nova instância da classe Task.

        Args:
            id (int): O ID da tarefa.
            title (str): O título da tarefa.
            description (str): A descrição da tarefa.
            completed (bool, opcional): O status de conclusão da tarefa.
                Por padrão, é False.
        """
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        """
        Converte a tarefa em um dicionário.

        Returns:
            dict: Um dicionário contendo as informações da tarefa.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }
