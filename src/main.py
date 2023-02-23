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
    print(json.dumps([dataclasses.asdict(e) for e in events], indent=4))
    for event in events:
        # Handle events
        pass


if __name__ == '__main__':
    main()
