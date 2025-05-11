"""
Tests for the hello_world function in the main.py module.
"""

import unittest
from unittest.mock import patch

from function.main import hello_world


class TestHelloWorld(unittest.TestCase):
    """Test cases for the hello_world function."""

    @patch("function.main.logging.info")
    def test_hello_world_logging(self, mock_logging_info):
        """Test that the function logs the expected message."""
        result = hello_world(None)

        mock_logging_info.assert_called_once_with("Devin demo: %s", "Hello, World!")

        self.assertEqual(result, "Hello, World!")

    def test_hello_world_return_value(self):
        """Test that the function returns the expected string."""
        result = hello_world(None)

        self.assertEqual(result, "Hello, World!")


if __name__ == "__main__":
    unittest.main()
