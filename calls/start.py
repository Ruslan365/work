from __future__ import print_function

import datetime
import os
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']
API_key = 'AIzaSyCEtMB04UgT0sc1abINROvlsU_AQjyWzVI'


def event_creator(attendees, event_time, broxus):
    event = {
        'description': 'Link to ds',
        'start': {
            'dateTime': str(event_time),
            'timeZone': 'Europe/Moscow',
        },
        'end': {
            'dateTime': str(event_time),
            'timeZone': 'Europe/Moscow',
        },
        'attendees': attendees,
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 240},
            ],
        },
    }

    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    event = service.events().insert(calendarId=broxus, body=event).execute()
    # 'Z' indicates UTC time
