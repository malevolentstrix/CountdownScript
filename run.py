import requests
import datetime
import requests
from discord import SyncWebhook


def scheduled_job():

    today = datetime.date.today()
    future = datetime.date(2023, 5, 31)
    diff = future - today
    day = diff.days
    temp = day
    if(day > 30):
        month = int(day/30)
        day = int(day % 30)

    # FOR TG
    base_url = 'https://api.telegram.org/bot5481709060:AAHiCCyL9ZISkf7iXl3w10hyK2Lt049XLfQ/sendMessage?chat_id=-601099314&text={}'.format(
        str(month) + " months " + str(day) + " days")
    requests.get(base_url)
    # FOR DISCORD
    webhook = SyncWebhook.from_url(
        "https://discord.com/api/webhooks/1013058619358597270/tbBUf22vy2fIbKo_K_bgIPuD6L57Z7ueWBrbvzXYS96bfWQyKmuE9XV0E3q-5Gjuf6GF")
    webhook.send(str(month) + " months " + str(day) + " days (" + str(temp) + " days)")


scheduled_job()
