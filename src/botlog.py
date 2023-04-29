"""
Handles logging of the bot.
"""

from datetime import datetime
from typing import Any


def botlog(*args: Any, **kwargs: Any) -> None:
    """
    A wrapper for the print function.

    The function prints first date and time string before printing the content of the
    argument. Then it prints a newline character.

    Keyword arguments are passed to the print function and they do not affect the
    date and time string.

    Example:
        >>> botlog("Hello World!")
        2023-03-09 10:06:36.763348  # Date and time string
        Hello World!  # The argument
          # Newline character

    Args:
        msg (str): Message to be logged. Newlines in the message argument
                   should be refrained from.
    """
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    print(f"{date_str}")
    print(*args, **kwargs)
    print()
