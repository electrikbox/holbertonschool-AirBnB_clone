#!/usr/bin/python3
""" Unittest for Amenity """

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import models

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_quit(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("quit")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, '')

    def test_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout2:
                self.console.onecmd(f"show BaseModel {output}")
                show_output = mock_stdout2.getvalue().strip()
                self.assertIn("BaseModel", show_output)

    def test_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout2:
                self.console.onecmd(f"destroy BaseModel {output}")
                destroy_output = mock_stdout2.getvalue().strip()
                self.assertFalse(destroy_output)

    def test_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all")
            all_output = mock_stdout.getvalue().strip()
            self.assertNotIn("BaseModel", all_output)
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all")
            all_output = mock_stdout.getvalue().strip()
            self.assertIn("BaseModel", all_output)

    def test_count(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create User")
            self.console.onecmd("create User")
            self.console.onecmd("create User")
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout2:
                self.console.onecmd("count User")
                count_output = mock_stdout2.getvalue().strip()
                self.assertEqual(count_output, "4")

    def test_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create User")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout2:
                self.console.onecmd(f"update User {output} last_name 'John'")
                self.console.onecmd(f"show User {output}")
                show_output = mock_stdout2.getvalue().strip()
                self.assertIn("'last_name': 'John'", show_output)

    def test_all_alt_syntax_1(self):
        models_list = [
            "BaseModel",
            "Review",
            "User",
            "State",
            "Amenity",
            "Place"
            ]
        for index in range(len(models_list)):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.console.onecmd(f"create {models_list[index]}")
                self.console.onecmd(f"{models_list[index]}.all()")
                all_output = mock_stdout.getvalue().strip()
                self.assertIn(f"{models_list[index]}", all_output)


if __name__ == '__main__':
    unittest.main()