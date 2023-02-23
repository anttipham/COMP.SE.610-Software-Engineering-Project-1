"""
This package handles Lyyti API requests.

The main use case is to call load_events which does all the work for
getting events and the participants.
"""
from .events import load_events, Event
from .participants import Participant
