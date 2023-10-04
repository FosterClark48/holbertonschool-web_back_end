#!/usr/bin/env python3
""" Unit Test module for client.py """

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from requests.cookies import MockResponse
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "my_license"}}, "other_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test the has_license static method of GOC """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration Test for GOC using fixtures.py """

    @classmethod
    def setUpClass(cls):
        """ Setup class """
        cls.get_patcher = patch('requests.get')

        # Create our mock instance
        cls.mock_get = cls.get_patcher.start()

        # Set up our mock to return our fixture data depending on input URL
        def side_effect(url):
            if url.endswith("/orgs/dummy_org"):
                return MockResponse(cls.org_payload)
            elif url.endswith("/orgs/dummy_org/repos"):
                return MockResponse(cls.repos_payload)
            else:
                return MockResponse({})

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """ Tear down class """
        cls.get_patcher.stop()

