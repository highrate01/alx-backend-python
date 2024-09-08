#!/usr/bin/env python3
"""
Unit test for access_nested_map function with parameterized inputs.
"""
import unittest
from utils import *
from parameterized import parameterized


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
