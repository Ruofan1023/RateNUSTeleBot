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
    response = requests.post(url, json=body)
    print(response.json())
    response_json = response.json()
    name_list = []
    content_list = response_json['content']
    for hostel in content_list:
        name_list.append(str(hostel['id']) + ". " + hostel['name'] + "\n")
    update.message.reply_text("".join(name_list))


hostel_list_command_handler = CommandHandler("hostels", hostel_list_command)
