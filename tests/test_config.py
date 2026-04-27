import unittest

from backend_journey.config import get_app_env


class ConfigTests(unittest.TestCase):
    def test_get_app_env_defaults_to_development(self) -> None:
        self.assertEqual(get_app_env(), "development")


if __name__ == "__main__":
    unittest.main()

