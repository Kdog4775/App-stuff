from __future__ import print_function
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import *
from gcsa.google_calendar import GoogleCalendar
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os.path
import datetime
from googleapiclient.discovery import build
from gcsa.event import Event

window = ThemedTk(theme="equilux")
window.config(themebg="equilux")
window.title("3D Printer Scheduler")
window.geometry('300x320')

nameLabel = ttk.Label(window, text="Name: Student ")
snumberLabel = ttk.Label(window, text="S-number: s1039522")

def clicked():
    calendar = GoogleCalendar('1039522km@gmail.com')
    for event in calendar:
        print(event)
SCOPES = ['https://www.googleapis.com/auth/calendar.events']
def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    def service(): build('calendar', 'v3', credentials=creds)
# Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
def service(): main()
def click():
    calendar = GoogleCalendar('1039522km@gmail.com, calendarId(PRIMARY)')
    event =



    

# credit goes to : https://google-calendar-simple-api.readthedocs.io/en/latest/events.html#create-event


#submitButton = ttk.Button(window, text="Submit", command=click)
#viewButton = ttk.Button(window, text="View Calendar", command=clicked)
# add labels and text entry/buttons to GUI
nameLabel.pack()
snumberLabel.pack()
#viewButton.pack(side=RIGHT)

window.mainloop()