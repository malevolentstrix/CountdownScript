import requests
import datetime


def scheduled_job():

    today = datetime.date.today()
    future = datetime.date(2023, 5, 31)
    diff = future - today
    day = diff.days
    if(day > 30):
        month = int(day/30)
        day = int(day % 30)

    print(int(month), int(day))
    base_url = 'https://api.telegram.org/bot5481709060:AAHiCCyL9ZISkf7iXl3w10hyK2Lt049XLfQ/sendMessage?chat_id=-601099314&text={}'.format(
        str(month) + " months " + str(day) + " days")
    requests.get(base_url)


scheduled_job()
