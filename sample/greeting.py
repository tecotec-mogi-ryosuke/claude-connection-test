"""接続テスト用のサンプルモジュール。"""

from __future__ import annotations

from datetime import time


class GreetingError(ValueError):
    """挨拶生成に失敗した場合に送出される例外。"""


def greet(name: str, *, now: time | None = None) -> str:
    """時刻に応じた挨拶文を返す。

    Args:
        name: 挨拶する相手の名前。空文字は許可しない。
        now: 判定に使う時刻。省略時は朝の挨拶を返す。

    Returns:
        「おはようございます、〇〇さん。」形式の挨拶文。

    Raises:
        GreetingError: name が空、または空白のみの場合。
    """
    trimmed = name.strip()
    if not trimmed:
        raise GreetingError("name must not be empty")

    return f"{_salutation(now or time(9, 0))}、{trimmed}さん。"


def _salutation(now: time) -> str:
    if now < time(11, 0):
        return "おはようございます"
    if now < time(18, 0):
        return "こんにちは"
    return "こんばんは"


if __name__ == "__main__":
    print(greet("モギ"))
    print(greet("モギ", now=time(13, 30)))
    print(greet("モギ", now=time(21, 0)))
