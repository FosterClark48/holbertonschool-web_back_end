#!/usr/bin/env python3
"""Unit Test module"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Test case for the function access_nested_map """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Paramaterized Unit test for access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Parameterized Unit test for access_nested_map
        Tests if function raises expected KeyError for specific inputs
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """ Test case for the function get_json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Test the get_json method with mocked HTTP calls. """
        # Mocking the response object that requests.get would have returned.
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function
        response = get_json(test_url)

        # Ensure the mocked get method was called with the right argument.
        mock_get.assert_called_once_with(test_url)

        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """ Test case for the function memoize """
    def test_memoize(self):
        """ Test the memoize decorator """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_class = TestClass()

        with patch.object(TestClass,
                          'a_method',
                          return_value=42) as mocked_a_method:
            result_1 = test_class.a_property
            result_2 = test_class.a_property

            mocked_a_method.assert_called_once()

            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)
