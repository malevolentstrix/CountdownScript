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


def writetosheet(dailylink1, dailylink2):
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
            'values': [[str(today-timedelta(days= 1)), dailylink1, dailylink2]],
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
    url = "https://api.telegram.org/bot5818771269:AAHlA8PtgxtwIRvVwR8KEDXiPFg5qQEtlvI/getUpdates"

    # Make a request to the API
    response = requests.get(url)
    #print(response.content)
    # Extract the message text from the response
    problems1 = ""
    problems2 = ""
    for i in response.json()["result"]:
        try:
            if i["message"]["reply_to_message"]["message_id"] == int(chatid_prevday):
                if i["message"]["from"]["id"]==1887210978:
                    message_text1 = i["message"]["text"]
                    print(i["message"]["from"]["id"]==1887210978)
                    problems1 += message_text1
                    problems1 += ", "
                if i["message"]["from"]["id"]==1887210978:
                    message_text2 = i["message"]["text"]
                    problems2 += message_text2
                    problems2 += ", "
            
        except KeyError as error:
            print(f"An error occurred: {error}")
    writetosheet(problems1[0:-2], problems2[0:-2])


    
    future = datetime.date(2023, 3, 28)
    diff =  today - future
    day = diff.days
    temp = day


    base_url1 = 'https://api.telegram.org/bot5818771269:AAHlA8PtgxtwIRvVwR8KEDXiPFg5qQEtlvI/sendMessage?chat_id=-817407338&text={}'.format(
        str(temp) + " days streak 🔥")
    base_url2 = 'https://api.telegram.org/bot5818771269:AAHlA8PtgxtwIRvVwR8KEDXiPFg5qQEtlvI/sendMessage?chat_id=-817407338&text={}'.format(
        str("Please share link to problems you've done today"))
    
    requests.get(base_url1)
    chatid = requests.get(base_url2).json()
    updateydaychatid(chatid["result"]["message_id"])
    print(chatid["result"]["message_id"])




scheduled_job()
