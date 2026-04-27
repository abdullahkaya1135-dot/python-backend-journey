import unittest

from backend_journey import get_health


class HealthTests(unittest.TestCase):
    def test_get_health_returns_ok_status(self) -> None:
        self.assertEqual(get_health(), {"status": "ok"})


if __name__ == "__main__":
    unittest.main()

