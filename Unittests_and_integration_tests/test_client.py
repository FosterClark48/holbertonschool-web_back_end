#!/usr/bin/env python3
""" Unit Test module for client.py """

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
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

    # patch.object is generally used to mock a property instead of patch
    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """ Test the _public_repos_url method of GOC """
        mock_org.return_value = {
            'repos_url': 'https://api.github.com/orgs/some_org/repos'}
        # Instantiate GOC
        client = GithubOrgClient("some_org")
        self.assertEqual(
            client._public_repos_url,
            'https://api.github.com/orgs/some_org/repos')

    @patch('client.get_json', return_value=[
        {"name": "repo1"},
        {"name": "repo2"},
        {"name": "repo3"}
    ])
    def test_public_repos(self, mock_get_json):
        """ Test the public_repos method of GOC """
        mock_payload = {"repos_url": "https://mocked_url.com"}
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = mock_payload["repos_url"]
            client = GithubOrgClient("dummy_thick_org")
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertListEqual(client.public_repos(), expected_repos)
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(mock_payload["repos_url"])
