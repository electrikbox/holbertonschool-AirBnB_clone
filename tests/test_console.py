#!/usr/bin/python3
""" Unittest for Amenity """

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

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
                self.assertEqual(count_output, "3")

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


if __name__ == '__main__':
    unittest.main()