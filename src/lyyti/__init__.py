"""
This package handles Lyyti API requests.

The main use case is to call load_events which does all the work for
getting events and the participants.
"""
from .events import Event, load_events
from .lyytirequest import get_events, get_participants
from .participants import Participant
