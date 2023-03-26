import requests
import datetime
from datetime import timedelta
import requests
from google.oauth2.service_account import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
today = datetime.date.today()

def authenticate():


    # Replace with the path to your service account JSON file
    creds = Credentials.from_service_account_file(
        './t2gd-352012-9f4db7e21863.json',
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )

    # Authenticate with the Google Sheets API
    service = build('sheets', 'v4', credentials=creds)
    return service


def writetosheet(dailylink):
    # Replace with the ID of your Google Sheet
    SPREADSHEET_ID = '1zpqe3bmrhTnmbgjPxHxZbNyGBaPx8OjlCpYIMW8w-qE'
    # Replace with the name of your sheet
    SHEET_NAME = 'Daily Status'

    service = authenticate()
    # Get the values of the first sheet
    try:
        result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=SHEET_NAME).execute()
        values = result.get('values', [])
    except HttpError as error:
        print(f"An error occurred: {error}")
        values = None

    # Get the range for the first empty row
    if values:
        next_row = len(values) + 1
    else:
        next_row = 1
    range_name = f"{SHEET_NAME}!A{next_row}"

    # Write the values to the sheet
    if range_name:
        body = {
            'values': [[str(today), dailylink]],
            'majorDimension': 'ROWS'
        }
        try:
            result = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID, range=range_name, valueInputOption='USER_ENTERED', body=body).execute()
            print(f"{result.get('updatedCells')} cells updated.")
        except HttpError as error:
            print(f"An error occurred: {error}")

def readydaychatid():
    service = authenticate()
    result = service.spreadsheets().values().get(spreadsheetId='1zpqe3bmrhTnmbgjPxHxZbNyGBaPx8OjlCpYIMW8w-qE', range='Chat_id!A1').execute()
    values = result.get('values', [])
    return values[0][0]
    #print(str(values[0][0]))

def updateydaychatid(id):
    service = authenticate()
    body = {
        'values': [[id]]
    }
    try:
        result = service.spreadsheets().values().update(spreadsheetId='1zpqe3bmrhTnmbgjPxHxZbNyGBaPx8OjlCpYIMW8w-qE', range='Chat_id!A1', valueInputOption='USER_ENTERED', body=body).execute()
        print(f"{result.get('updatedCells')} cells updated.")
    except HttpError as error:
        print(f"An error occurred: {error}")
    return result


def scheduled_job():
    chatid_prevday = readydaychatid()
    print(chatid_prevday)
    # Check yesterday's problem solution
    url = "https://api.telegram.org/bot5481709060:AAHiCCyL9ZISkf7iXl3w10hyK2Lt049XLfQ/getUpdates"

    # Make a request to the API
    response = requests.get(url)
   # print(response.content)
    # Extract the message text from the response
    problems = ""
    for i in response.json()["result"]:
        try:
            if i["message"]["reply_to_message"]["message_id"] == int(chatid_prevday):
                message_text = i["message"]["text"]
                print(message_text)
                problems += message_text
                problems += ", "
        except KeyError as error:
            print(f"An error occurred: {error}")
    writetosheet(problems[0:-2])


    
    future = datetime.date(2023, 6, 25)
    diff = future - today
    day = diff.days
    temp = day
    if (day > 30):
        month = int(day/30)
        day = int(day % 30)


    base_url1 = 'https://api.telegram.org/bot5481709060:AAHiCCyL9ZISkf7iXl3w10hyK2Lt049XLfQ/sendMessage?chat_id=-945979691&text={}'.format(
        str(month) + " months " + str(day) + " days (" + str(temp) + " days) for Placement Day " + str(future))
    base_url2 = 'https://api.telegram.org/bot5481709060:AAHiCCyL9ZISkf7iXl3w10hyK2Lt049XLfQ/sendMessage?chat_id=-945979691&text={}'.format(
        str("Please share link to problems you've done today"))
    
    requests.get(base_url1)
    chatid = requests.get(base_url2).json()
    updateydaychatid(chatid["result"]["message_id"])
    print(chatid["result"]["message_id"])




scheduled_job()
