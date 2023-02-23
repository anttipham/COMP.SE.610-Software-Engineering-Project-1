"""
Univincity-throw-in-bot
"""
import dataclasses
import json

import lyyti


def main():
    """
    Main function
    """
    events = lyyti.load_events()
    # Printing the events in a nice format.
    print("Events:\n")
    print(json.dumps([dataclasses.asdict(e) for e in events], indent=4))

    # Printing the participants of each event in nice format.
    print("Event participants:\n")

    for event in events:
        print(f"Event: {event.event_id}\nParticipants:", end=" ")
        for participant in event.participants:
            print(participant.email, end=" || ")
        print()


if __name__ == "__main__":
    main()
