"""
Sets variables to environment variables for testing purposes.
"""
import os

if 'LYYTI_PRIVATE_KEY' not in os.environ:
    os.environ['LYYTI_PRIVATE_KEY'] = '<PRIVATE KEY HERE>'

if 'LYYTI_PUBLIC_KEY' not in os.environ:
    os.environ['LYYTI_PUBLIC_KEY'] = '<PUBLIC KEY HERE>'

if 'TIMEOUT_DURATION' not in os.environ:
    os.environ['TIMEOUT_DURATION'] = '10'

if 'LYYTI_ROOT_URL' not in os.environ:
    os.environ['LYYTI_ROOT_URL'] = 'https://api.lyyti.com/v2/'

if 'LYYTI_EVENTS_CALLSTRING' not in os.environ:
    os.environ['LYYTI_EVENTS_CALLSTRING'] = 'events/'

if 'LYYTI_PARTICIPANTS_CALLSTRING' not in os.environ:
    os.environ['LYYTI_PARTICIPANTS_CALLSTRING'] = 'participants/{}'

if 'LYYTI_EVENTS_RESPONSE' not in os.environ:
    with open('../res/events-sample.json', 'r', encoding='utf-8') as f:
        os.environ['LYYTI_EVENTS_RESPONSE'] = f.read()

if 'LYYTI_PARTICIPANTS_RESPONSE' not in os.environ:
    with open('../res/participants-sample.json', 'r', encoding='utf-8') as f:
        os.environ['LYYTI_PARTICIPANTS_RESPONSE'] = f.read()
