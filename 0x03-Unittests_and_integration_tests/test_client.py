#!/usr/bin/env python3
"""
Module that contain test class
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import *
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"org": "Google"}),
        ("abc", {"org": "ABC"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_payload, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        Ensure that get_json is called once with the correct URL.
        """
        # Sets up the mock to return the expected payload
        mock_get_json.return_value = expected_payload

        # Creates a client instance for the given org_name
        client = GithubOrgClient(org_name)

        self.assertEqual(client.org, expected_payload)
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"}),
    ])
    def test_public_repos_url(self, org_name, expected_payload):
        """
        Test that the result of _public_repos_url is the expected one
        based on the mocked payload.
        """
        with patch.object(
                GithubOrgClient, 'org', new_callable=unittest.mock.PropertyMock
                ) as mock_org:
            mock_org.return_value = expected_payload
            client = GithubOrgClient(org_name)
            result = client._public_repos_url
            self.assertEqual(result, expected_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos"""

        mock_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}}
        ]

        expected_repos = ["repo1", "repo2", "repo3"]

        mock_get_json.return_value = mock_repos_payload

        with patch.object(
                GithubOrgClient, '_public_repos_url', new_callable=PropertyMock
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = \
                    "https://api.github.com/orgs/google/repos"

            client = GithubOrgClient("google")

            repos = client.public_repos()

            self.assertEqual(repos, expected_repos)

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                    "https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
        [
            {
                "org_payload": TEST_PAYLOAD[0][0],
                "repos_payload": TEST_PAYLOAD[0][1],
                "expected_repos": TEST_PAYLOAD[0][2],
                "apache2_repos": TEST_PAYLOAD[0][3],
                }
            ]
        )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class."""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
