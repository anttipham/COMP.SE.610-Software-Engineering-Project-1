import functools
import logging

"""Configure logging. Change the level to see more logs. (DEBUG, INFO, WARNING, ERROR, CRITICAL))"""
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def log_exception(function):
    """
    Simple logger decorator for logging exeptions.
    It logs the exception and raises it again.
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            logger.exception(f"There was an exception in {function.__name__}: {e}")
            raise e

    return wrapper


def clientErrorHandler():
    """
    Handles such errors that has status code between 400-499.
    """
    print("Not implemented")


def serverErrorHandler():
    """
    Handles such errors that has status code between 500-599.
    """
    print("Not implemented")
