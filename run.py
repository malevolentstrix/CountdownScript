import requests

def scheduled_job():
    base_url = 'https://api.telegram.org/bot5481709060:AAHiCCyL9ZISkf7iXl3w10hyK2Lt049XLfQ/sendMessage?chat_id=-601099314&text={}'.format(
        "Heyo Helo")
    requests.get(base_url)

scheduled_job()
