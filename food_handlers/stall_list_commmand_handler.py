import requests
from telegram.ext import *

url = 'https://www.ratenus.cyou:8080/stall'


def stall_list_command(update, context):
    body = {
        "orderBy": "id",
        "isLowToHigh": True,
        "pageNum": 0,
        "pageSize": 100
    }
    response = requests.post(url, json=body)
    response_json = response.json()
    name_list = []
    content_list = response_json['content']
    for food in content_list:
        name_list.append(str(food['id']) + ". " + food['name'] + "\n")
    update.message.reply_text("Which restaurant would you like to see?\nReply with /food + id :)")
    update.message.reply_text("".join(name_list))


stall_list_command_handler = CommandHandler("foods", stall_list_command)
