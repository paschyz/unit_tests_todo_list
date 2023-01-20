from datetime import datetime, timedelta
from modules.todo_item import TodoItem
from modules.email_sender_service import EmailSenderService


class TodoList:
    def __init__(self):
        self.items = []
        self.item_names = set()
        self.last_item_creation_time = None
        self.email_sender = EmailSenderService()

    def set_list(self, items):
        self.items = items
        self.item_names = set()
        for item in self.items:
            self.item_names.add(item.name)
        self.last_item_creation_time = None
        if len(self.items) > 0:
            self.last_item_creation_time = self.items[-1].date_created

    def add_item(self, item_name, item_content, item_state, user):
        if item_name in self.item_names:
            raise Exception("Item name already exists.")
        if len(item_content) > 1000:
            raise Exception("Item content is too long.")
        if len(self.items) >= 10:
            raise Exception("TodoList max size of 10 exceeded.")
        if self.last_item_creation_time is not None and self.last_item_creation_time + timedelta(minutes=30) > datetime.now():
            raise Exception("Cannot add item. Wait for 30 minutes.")

        self.last_item_creation_time = datetime.now()
        item = TodoItem(item_name, item_content, item_state,
                        self.last_item_creation_time)
        self.items.append(item)
        self.item_names.add(item_name)

        if len(self.items) == 8:
            self.email_sender.send(
                user.email, "You have 8 items in your todo list. You have 2 items left to add.", "Lorem ipsum")
