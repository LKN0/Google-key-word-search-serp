import unittest
from unittest.mock import patch, MagicMock
import requests
from app import get_google_results


class TestKeywordSearcher(unittest.TestCase):

    @patch("app.requests.get")
    def test_get_google_results_success(self, mock_get):
        """Testuje správné zpracování dat z API bez reálného volání sítě."""
        # 1. Připravíme falešnou odpověď ze SerpAPI
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

        # 2. Zavoláme naši funkci
        results = get_google_results("python")

        # 3. Ověříme výsledek
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 1)

        first_item = results[0]
        self.assertEqual(first_item["position"], 1)
        self.assertEqual(first_item["title"], "Python Official Site")
        self.assertEqual(first_item["link"], "https://www.python.org")
        self.assertEqual(first_item["snippet"], "Official website of Python programming language.")

        # Ověříme, že requests.get byl skutečně zavolán
        mock_get.assert_called_once()

    @patch("app.requests.get")
    def test_get_google_results_network_failure(self, mock_get):
        """Testuje, že aplikace nespadne při výpadku sítě, ale vrátí prázdný seznam."""
        # Simulujeme pád sítě (vyvolání výjimky)
        mock_get.side_effect = requests.RequestException("Chyba spojení se serverem")

        results = get_google_results("test")

        # Aplikace nesmí spadnout s chybou, ale vrátit []
        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()
