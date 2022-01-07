import requests
from telegram.ext import *

url = 'https://www.ratenus.cyou:8080/hostel'


def hostel_list_command(update, context):
    body = {
        "orderBy": "id",
        "isLowToHigh": True,
        "pageNum": 0,
        "pageSize": 100
    }
    response = requests.post(url, data=body)
    print(str(response))
    update.message.reply_text(response)


hostel_list_command_handler = CommandHandler("hostels", hostel_list_command)
