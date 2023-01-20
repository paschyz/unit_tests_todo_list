import unittest
from datetime import datetime
from modules import TodoItem


class TestTodoItem(unittest.TestCase):
    def test_create_todo_item(self):
        item_name = "Test Item"
        item_content = "This is a test item"
        item_state = "Not started"
        item_date = datetime.now()
        item = TodoItem(item_name, item_content, item_state, item_date)

        self.assertEqual(item.name, item_name)
        self.assertEqual(item.content, item_content)
        self.assertEqual(item.state, item_state)
        self.assertEqual(item.date_created, item_date)
