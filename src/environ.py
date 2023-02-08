"""
Sets variables to environment variables for testing purposes.
"""
import os

if 'TIMEOUT_DURATION' not in os.environ:
    os.environ['TIMEOUT_DURATION'] = '10'

if 'LYYTI_EVENTS_URL' not in os.environ:
    os.environ['LYYTI_EVENTS_URL'] = 'https://api.lyyti.com/v2/events/'

if 'LYYTI_PARTICIPANTS_URL' not in os.environ:
    os.environ['LYYTI_PARTICIPANTS_URL'] = \
      'https://api.lyyti.com/v2/participants/{}'

if 'LYYTI_EVENTS_RESPONSE' not in os.environ:
    os.environ['LYYTI_EVENTS_RESPONSE'] = '''
{
  "method": "GET",
  "call": "events",
  "parameters": {},
  "results": {
    "eed1b509f8abbb0": {
      "eid": 1073902,
      "id": "eed1b509f8abbb0",
      "event_id": 1073902,
      "event_code": "eed1b509f8abbb0",
      "company_id": 7219,
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
    "1073902-1849831122": {
      "id": 1849835123,
      "group": null,
      "participants": [
        {
          "id": 1849835123,
          "uid": "1073902-1849831122",
          "group_id": null,
          "is_contact_person": 0,
          "email": "firstname.lastname@vincit.fi",
          "email_blocked": 0,
          "firstname": "John",
          "lastname": "Doe",
          "lang": "en",
          "status": "reactedyes",
          "queue_status": null,
          "queue_enter_time": null,
          "queue_position": null,
          "participant_type": null,
          "is_active": 1,
          "is_avec": 0,
          "has_avec": 0,
          "phone": "040123123",
          "phone_countrycode": "358",
          "online_event_link": null,
          "timestamp_added": 1660118292,
          "timestamp_enrolled": 1660118398,
          "timestamp_modified": 1675848902,
          "info1": null,
          "info2": null,
          "organiser_info": null,
          "matches": 1,
          "answers": [],
          "payments": null
        }
      ]
    },
    "1073902-1096672233": {
      "id": 1096675123,
      "group": null,
      "participants": [
        {
          "id": 1096675123,
          "uid": "1073902-1096672233",
          "group_id": null,
          "is_contact_person": 0,
          "email": "firstname2.lastname2@vincit.fi",
          "email_blocked": 0,
          "firstname": "John2",
          "lastname": "Doe2",
          "lang": "en",
          "status": "reactedyes",
          "queue_status": null,
          "queue_enter_time": null,
          "queue_position": null,
          "participant_type": null,
          "is_active": 1,
          "is_avec": 0,
          "has_avec": 0,
          "phone": "50112233",
          "phone_countrycode": "358",
          "online_event_link": null,
          "timestamp_added": 1660143416,
          "timestamp_enrolled": 1660143475,
          "timestamp_modified": 1660143475,
          "info1": null,
          "info2": null,
          "organiser_info": null,
          "matches": 1,
          "answers": [],
          "payments": null
        }
      ]
    }
  },
  "results_count": 2,
  "parent": "https://www.lyyti.fi/api/v2/participants",
  "url": "https://www.lyyti.fi/api/v2/participants/1073902"
}
'''
