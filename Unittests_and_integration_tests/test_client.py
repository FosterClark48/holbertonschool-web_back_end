#!/usr/bin/env python3
""" Unit Test module for client.py """

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestAccessNestedMap(unittest.TestCase):
    """ Test case for the GithubOrgClient class """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """ Tests that GithubOrgClinet.org returns correct value """
        # Create instance of GOC w/ given org name
        github_org_client = GithubOrgClient(org_name)
        # Set mock return value
        mock_get_json.return_value = {"fake_key": "fake_value"}
        # Call org method of GOC instance
        response = github_org_client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(response, {"fake_key": "fake_value"})
