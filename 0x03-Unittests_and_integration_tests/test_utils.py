#!/usr/bin/env python3
"""
Unit test for access_nested_map function with parameterized inputs.
"""
import unittest
from utils import *
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for the access_nested_map function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        """
        Test that access_nested_map returns the expected value
        for a given path.
        """
        self.assertEqual(access_nested_map(nested_map, path),
                         expected_value)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test if keyError is raised for parameterized_expand
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    tests if tils.get_json returns the expected result.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that utils.get_json returns the expected result
        and that requests.get was called with the correct URL
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    tests case for memoize decorator
    """
    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_method):
        """
        Test that a_method is only called once even when
        a_property is accessed multiple times.
        """
        test_instance = self.TestClass()

        # Call a_property twice
        result_1 = test_instance.a_property
        result_2 = test_instance.a_property

        # Check that the result is correct both times
        self.assertEqual(result_1, 42)
        self.assertEqual(result_2, 42)

        # Ensure that a_method was only called once due to memoization
        mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
