"""greeting モジュールのテスト。"""

from __future__ import annotations

import unittest
from datetime import time

from greeting import GreetingError, greet


class GreetTest(unittest.TestCase):
    def test_morning(self) -> None:
        self.assertEqual(greet("モギ", now=time(9, 0)), "おはようございます、モギさん。")

    def test_afternoon(self) -> None:
        self.assertEqual(greet("モギ", now=time(13, 30)), "こんにちは、モギさん。")

    def test_evening(self) -> None:
        self.assertEqual(greet("モギ", now=time(21, 0)), "こんばんは、モギさん。")

    def test_default_is_morning(self) -> None:
        self.assertEqual(greet("モギ"), "おはようございます、モギさん。")

    def test_name_is_trimmed(self) -> None:
        self.assertEqual(greet("  モギ  "), "おはようございます、モギさん。")

    def test_blank_name_raises(self) -> None:
        for invalid in ("", "   "):
            with self.subTest(name=invalid):
                with self.assertRaises(GreetingError):
                    greet(invalid)


if __name__ == "__main__":
    unittest.main()
