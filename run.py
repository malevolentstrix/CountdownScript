import requests
import datetime
import requests
import json
# from discord import SyncWebhook


def scheduled_job():

    today = datetime.date.today()
    future = datetime.date(2023, 6, 20)
    diff = future - today
    day = diff.days
    temp = day
    if(day > 30):
        month = int(day/30)
        day = int(day % 30)

    # FOR TG
    base_url2 = 'https://api.telegram.org/bot5481709060:AAHiCCyL9ZISkf7iXl3w10hyK2Lt049XLfQ/sendMessage?chat_id=-601099314&text={}'.format(
        str(month) + " months " + str(day) + " days (" + str(temp) + " days) for " + str(future))

    base_url = 'https://api.telegram.org/bot5481709060:AAHiCCyL9ZISkf7iXl3w10hyK2Lt049XLfQ/sendPoll'

    parameters = {
        "chat_id" : "-601099314",
        "question" : "To do",
        # Regular Day
        # "options" : json.dumps(["Solve 10 LeetCode Problems", "Solve 10 Aptitude Problems", "Learn AWS", "Read 10 Pages", "Speak 15 mins", "Solve Rubiks Cube"]),
        
        # Rush Days
        "options" : json.dumps(["Final Year Project", "Wordle", "Photo Album", "Tic Tac Toe", "Exam Prep"]),
        "allows_multiple_answers" : True
    }

    resp = requests.get(base_url, data = parameters)
    print(resp)

    requests.get(base_url2)
    # FOR DISCORD
    # webhook = SyncWebhook.from_url(
    #     "https://discord.com/api/webhooks/1013058619358597270/tbBUf22vy2fIbKo_K_bgIPuD6L57Z7ueWBrbvzXYS96bfWQyKmuE9XV0E3q-5Gjuf6GF")
    # webhook.send(str(month) + " months " + str(day) + " days (" + str(temp) + " days)")


scheduled_job()
