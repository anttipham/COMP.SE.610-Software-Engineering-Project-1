import time


def hi():
    print("Hi!")


# maybe the simplest timer that runs given function at given intervals
def run_with_interval(function: callable, interval: float):
    while True:
        function()
        time.sleep(interval)


run_with_interval(hi, 5)
