import unittest
import datetime
from datetime import date, timedelta
from datetime import datetime as dt
from unittest.mock import Mock, patch
from modules import EmailSenderService
from modules import TodoList
from modules import TodoItem
from modules import User


class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.user = User("example@gmail.com", "John", "Doe",
                         "Pa$$word1", date(2000, 1, 1))
        self.list = TodoList(self.user)

    def test_add_item(self):
        self.list.add_item("Test Item", "This is a test item", "not_started")
        self.assertEqual(len(self.list.items), 1)

    def test_add_item_invalid_user(self):
        self.user.password = "pass1"
        with self.assertRaises(Exception) as context:
            self.list.add_item(
                "Test Item", "This is a test item", "not_started")
        self.assertEqual("User is not valid.", str(context.exception))

    def test_add_item_too_soon(self):
        self.list.add_item("Test Item", "This is a test item",
                           "not_started")
        with self.assertRaises(Exception) as context:
            self.list.add_item(
                "Test Item 2", "not_started", "not_started")
        self.assertEqual("Cannot add item. Wait for 30 minutes.",
                         str(context.exception))

    def test_add_item_name_already_exists(self):
        self.list.add_item("Test Item", "This is a test item",
                           "not_started")
        with self.assertRaises(Exception) as context:
            self.list.add_item(
                "Test Item", "This is a test item", "not_started")
        self.assertEqual("Item name already exists.", str(context.exception))

    @patch('modules.todo_list.EmailSenderService')
    def test_send_email_after_8_items(self, mock_email_sender):
        mock_email_sender = Mock(EmailSenderService)
        self.list.email_sender = mock_email_sender

        items = []
        for i in range(7):
            items.append(TodoItem("Test Item " + str(i),
                         "This is a test item", "not_started", dt.now() - timedelta(minutes=30)))

        self.list.set_list(items)
        assert len(self.list.items) == 7
        self.list.add_item("Test Item 8", "This is a test item", "not_started")
        assert len(self.list.items) == 8
        mock_email_sender.send.assert_called_once_with(
            self.user.email, "You have 8 items in your todo list. You have 2 items left to add.", "Lorem ipsum")

    def test_add_item_list_size_exceeded(self):
        items = []
        for i in range(10):
            items.append(TodoItem("Test Item " + str(i),
                         "This is a test item", "not_started", dt.now() - timedelta(minutes=30)))
        self.list.set_list(items)
        with self.assertRaises(Exception) as context:
            self.list.add_item(
                "Test Item 10", "not_started", "not_started")
        self.assertEqual("TodoList max size of 10 exceeded.",
                         str(context.exception))
