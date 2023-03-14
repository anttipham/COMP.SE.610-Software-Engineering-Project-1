"""
Handles logging of the bot.
"""

from datetime import datetime


def botlog(msg: str) -> None:
    """
    Logs the message argument in the format, wanted by the customer.

    Adds date and time string to the front of the message argument and
    prints it to stdout.

    An example of the date and time string is "2023-03-09 10:06:36.763348".

    Args:
        msg (str): Message to be logged. Newlines in the message argument
                   should be refrained from.
    """
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    print(f"{date_str} {msg}")
