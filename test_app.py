import unittest
from unittest.mock import patch, MagicMock
import requests
from app import get_google_results


class TestKeywordSearcher(unittest.TestCase):

    @patch("app.requests.get")
    def test_get_google_results_success(self, mock_get):
        """Test successful parsing of SerpAPI search results without hitting the network."""
        # 1. Prepare mocked response from SerpAPI
        fake_response = MagicMock()
        fake_response.json.return_value = {
            "organic_results": [
                {
                    "position": 1,
                    "title": "Python Official Site",
                    "link": "https://www.python.org",
                    "snippet": "Official website of Python programming language."
                }
            ]
        }
        fake_response.raise_for_status.return_value = None
        mock_get.return_value = fake_response

        # 2. Call the function under test
        results = get_google_results("python")

        # 3. Assert the parsed structure
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 1)

        first_item = results[0]
        self.assertEqual(first_item["position"], 1)
        self.assertEqual(first_item["title"], "Python Official Site")
        self.assertEqual(first_item["link"], "https://www.python.org")
        self.assertEqual(first_item["snippet"], "Official website of Python programming language.")

        # Verify requests.get was invoked once
        mock_get.assert_called_once()

    @patch("app.requests.get")
    def test_get_google_results_network_failure(self, mock_get):
        """Test that network exceptions are handled gracefully and return an empty list."""
        # Simulate network failure by raising RequestException
        mock_get.side_effect = requests.RequestException("Connection to remote server failed")

        results = get_google_results("test")

        # Function should catch exception and return an empty list instead of crashing
        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()
