from datetime import datetime


class TodoItem:
    def __init__(self, name, content, state, date_created=datetime.now()):
        self.name = name
        self.content = content
        self.state: bool = state
        self.date_created = date_created

    def __str__(self):
        return f"Name: {self.name}, Content: {self.content}, State: {self.state}, Date Created: {self.date_created}"
