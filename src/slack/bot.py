

def send_slack_message(message: str):
    '''
    Send a message to our Slack channel.
    '''
    import requests
    payload = '{"text": "%s"}' % message
    response = requests.post(
        "https://hooks.slack.com/services/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",
        data = payload
    )
    print(response.text)

def main(message_text: str):
    '''
    Main function where we can to build our logic
    '''
    send_slack_message(message=message_text)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Send messages to Slack")
    parser.add_argument('--message','-m', type=str,default='')
    args = parser.parse_args()

    msg = args.message

    if len(msg) > 0:
        main(message_text=msg)
    
    else:
        print("Give me a message")