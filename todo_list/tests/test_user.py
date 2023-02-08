import unittest
import datetime
from modules import User


class TestUser(unittest.TestCase):
    def test_valid_user(self):
        user = User("example@gmail.com", "John", "Doe",
                    "Pa$$word1", datetime.date(2000, 1, 1))
        self.assertTrue(user.is_valid())

    def test_invalid_user_password_too_short(self):
        user = User("example@gmail.com", "John", "Doe",
                    "Pass1", datetime.date(2000, 1, 1))
        self.assertFalse(user.is_valid())

    def test_invalid_no_firstname(self):
        user = User("example@gmail.com", "", "Doe",
                    "Pa$$word1", datetime.date(2000, 1, 1))
        self.assertFalse(user.is_valid())

    def test_invalid_no_lastname(self):
        user = User("example@gmail.com", "John", "",
                    "Pa$$word1", datetime.date(2000, 1, 1))
        self.assertFalse(user.is_valid())

    def test_invalid_user_password_no_uppercase(self):
        user = User("example@gmail.com", "John", "Doe",
                    "password1", datetime.date(2000, 1, 1))
        self.assertFalse(user.is_valid())

    def test_invalid_user_password_no_digit(self):
        user = User("example@gmail.com", "John", "Doe",
                    "Password", datetime.date(2000, 1, 1))
        self.assertFalse(user.is_valid())

    def test_invalid_user_email(self):
        user = User("example.com", "John", "Doe",
                    "Pa$$word1", datetime.date(2000, 1, 1))
        self.assertFalse(user.is_valid())

    def test_invalid_user_too_young(self):
        user = User("example@gmail.com", "John", "Doe",
                    "Pa$$word1", datetime.date(2012, 1, 1))
        self.assertTrue(user.is_valid())
