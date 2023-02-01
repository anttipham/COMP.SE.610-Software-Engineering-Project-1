"""
Timer module that runs a function at a given interval.
"""

import time
from typing import Callable


def run_with_interval(function: Callable, interval: float):
    """
    Timer that runs a function in a given interval.

    Args:
        function (Callable): Function to run in a given interval.
        interval (float): Interval in minutes to execute the function.
    """
    while True:
        function()
        time.sleep(interval * 60)
