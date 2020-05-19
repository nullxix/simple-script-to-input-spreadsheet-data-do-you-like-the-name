from __future__ import print_function
import pickle
import os.path
import config
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file google_token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def upload(upload_data: [list], sheet_name: str, sheet_id: str, tab_name: str, test_col: str = 'A',):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    PICKLE_FILE = 'google_token-' + sheet_name +  '.pickle'
    # The file google_token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(PICKLE_FILE):
        with open(PICKLE_FILE, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'google-api-credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(PICKLE_FILE, 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Find the first row without a student name
    sheet_values = service.spreadsheets().values()
    result = sheet_values.get(spreadsheetId=sheet_id,
                                range=tab_name + '!' + test_col + ':' + test_col,
                                ).execute()
    values = result.get('values', [])
    first_empty = len(values) + 1

    print('Aim cannons at:',  first_empty)

    #prep the write
    widest_array = 0
    for row in upload_data:
        if widest_array < len(row):
            widest_array = len(row)

    end_range = alphabet[widest_array] + str(len(upload_data) + first_empty)
    write_range = str(tab_name) + '!A' + str(first_empty) + ':' + end_range
    print('writing to range:', write_range)
    #write it
    sheet_values.update(spreadsheetId = sheet_id,
                        range = write_range,
                        body = {
                            'range': write_range,
                            'values': upload_data,
                            'majorDimension': "ROWS",
                        },
                        valueInputOption = "USER_ENTERED",
                        ).execute()

    # start filling in data beneath that
    

if __name__ == '__main__':
    upload(
        [["This has been a test!", "MORE TEST"], ["Also a test!"]], 
        sheet_name = 'test',
        sheet_id = '1s11c-vbUR7QPdUNUX5cymPW0e4Jj_4Aa6RbGVCZ2yII', 
        tab_name = 'main' )