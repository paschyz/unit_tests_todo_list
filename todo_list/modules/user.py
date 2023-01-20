import datetime
import re

from modules.todo_list import TodoList


class User:
    def __init__(self, email, firstname, lastname, password, birthdate):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.birthdate = birthdate
        self.todo_list: TodoList = None

    def is_valid(self):
        if self.firstname == "":
            return False
        if self.lastname == "":
            return False
        if not (8 <= len(self.password) <= 40):
            return False
        if not any(c.isupper() for c in self.password):
            return False
        if not any(c.isdigit() for c in self.password):
            return False
        if not self.is_valid_email():
            return False
        if not self.is_old_enough():
            return False
        return True

    def set_todo_list(self, todo_list):
        self.todo_list = todo_list

    def get_todo_list(self):
        return self.todo_list

    def is_old_enough(self):
        # must be at least 13 years old
        today = datetime.date.today()
        age = today.year - self.birthdate.year - \
            ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age >= 13

    def is_valid_email(self):
        # use a regex to check if the email is valid
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(regex, self.email)
