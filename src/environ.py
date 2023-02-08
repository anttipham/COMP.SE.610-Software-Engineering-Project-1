"""
Sets variables to environment variables for testing purposes.
"""
import os


if 'TIMEOUT_DURATION' not in os.environ:
    os.environ['TIMEOUT_DURATION'] = '10'

if 'LYYTI_EVENTS_URL' not in os.environ:
    os.environ['LYYTI_EVENTS_URL'] = 'https://api.lyyti.com/v2/events/'

if 'LYYTI_PARTICIPANTS_URL' not in os.environ:
    os.environ['LYYTI_PARTICIPANTS_URL'] = 'https://api.lyyti.com/v2/participants/{}'

if 'LYYTI_EVENTS_RESPONSE' not in os.environ:
    os.environ['LYYTI_EVENTS_RESPONSE'] = '''
{
  "method": "GET",
  "call": "events",
  "parameters": {},
  "results": {
    "abc123": {
      "eid": 123,
      "id": "abc123",
      "event_id": 123,
      "event_code": "abc123",
      "company_id": 456,
      "owner_id": 789,
      "owner": "clark.kent@dailyplanet.com",
      "owner_name": "Clark Kent",
      "relationship": "company",
      "start_time_utc": 1583100000,
      "end_time_utc": 1717189200,
      "enrollment_open_utc": 1574460000,
      "enrollment_deadline_utc": 1760562000,
      "canceling_deadline_utc": 1760562000,
      "editing_deadline_utc": 1760389200,
      "timezone": "Europe/Helsinki",
      "start_time": 1460556000,
      "end_time": 1460638800,
      "enrollment_open": 1444338000,
      "enrollment_deadline": 1459760400,
      "canceling_deadline": 1456783140,
      "editing_deadline": 1458338340,
      "created_utc": 1596430825,
      "modified_utc": 1622642701,
      "archived": 0,
      "payable": 0,
      "queue": null,
      "enrollment_type": "single",
      "open_code": "weekly_meeting_32_A123",
      "enrollment_url": "https://www.lyyti.in/weekly_meeting_32_A123",
      "eventsite_url": null,
      "layout_id": 1234,
      "map_link": "https://www.google.com/maps/search/?api=1&query=address",
      "participant_capacity": null,
      "participant_count": 12,
      "participant_counts": {
        "show": 6,
        "noshow": 3,
        "reactedyes": 3,
        "reactedno": 0,
        "notreacted": 0
      },
      "unconfirmed_count": 0,
      "group_capacity": null,
      "group_count": null,
      "participant_types": null,
      "location_type": "hybrid",
      "online_event_link": "https://www.lyyti.fi",
      "reservation_time_limit": 20,
      "shared_rights": null,
      "language": [
        "en"
      ],
      "name": {
        "en": "Weekly Meeting 32"
      },
      "location": {
        "en": "5th floor, meeting room"
      },
      "address": {
        "en": "123 Street Av., 54321 Metropolis"
      },
      "homepage": {
        "en": ""
      },
      "homepage_title": {
        "en": ""
      },
      "participant_type_heading": {
        "en": "Participant type"
      },
      "online_event_link_title": {
        "en": "Lyyti"
      },
      "contact_person": {
        "en": {
          "name": "Clark Kent",
          "email": "clark.kent@dailyplanet.com"
        }
      },
      "has_participants": 1,
      "category": {
        "1": {
          "id": 555,
          "title": "Private Calendar"
        },
        "2": {
          "id": 567,
          "title": "Internal Meetings"
        }
      },
      "custom": {
        "230": {
          "id": 456,
          "title": "Internal ID",
          "answer": 9876
        }
      },
      "participants": "https://api.lyyti.com/v2/events/abc123/participants",
      "questions": "https://api.lyyti.com/v2/events/abc123/questions",
      "url": "https://api.lyyti.com/v2/events/abc123"
    }
  },
  "results_count": 1,
  "parent": "https://api.lyyti.com/v2",
  "url": "https://api.lyyti.com/v2/events"
}
'''

if 'LYYTI_PARTICIPANTS_RESPONSE' not in os.environ:
    os.environ['LYYTI_PARTICIPANTS_RESPONSE'] = '''
{
  "results": {
    "55845-715819602": {
      "id": 715819602,
      "group": null,
      "participants": [
        {
          "id": 715819602,
          "uid": "55845-715819602",
          "group_id": null,
          "is_contact_person": 0,
          "email": "care@lyyti.fi",
          "email_blocked": 0,
          "firstname": "Test",
          "lastname": "Participant",
          "lang": "fi",
          "status": "reactedyes",
          "participant_type": 0,
          "is_avec": 0,
          "has_avec": 0,
          "phone": "",
          "phone_countrycode": 358,
          "timestamp_added": 1397634328,
          "timestamp_enrolled": 1397634410,
          "timestamp_modified": 1397634398,
          "info1": null,
          "info2": null,
          "organiser_info": null,
          "answers": {
            "782878": {
              "649445": 8,
              "649446": 16,
              "649447": 17,
              "649448": 5
            },
            "782895": "Linnankatu 13 Aa 18",
            "782896": 20100,
            "782897": "Turku"
          },
          "payments": {
            "payment_method": "invoice",
            "payments_open": 40.4,
            "payments_paid": 0,
            "payments_total": 40.4
          }
        }
      ]
    }
  },
  "results_count": 1,
  "parent": "https://www.lyyti.fi/api/v2/participants",
  "url": "https://www.lyyti.fi/api/v2/participants/55845"
}
'''
