#!/usr/bin/env python3
"""
Module that contain test class
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import *


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


if __name__ == "__main__":
    unittest.main()
