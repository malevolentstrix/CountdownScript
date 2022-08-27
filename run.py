import requests

def scheduled_job():
    base_url = 'https://api.telegram.org/bot2082575294:AAG6pW-7k9bOI6AmgMYqNnINPvG8M6NeKqY/sendMessage?chat_id=-601394167&text={}'.format(
        "Heyo Helo")
    requests.get(base_url)

scheduled_job()
