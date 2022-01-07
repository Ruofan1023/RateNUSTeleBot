import requests
from telegram.ext import *

url = 'https://www.ratenus.cyou:8080/studyArea'


def study_area_list_command(update, context):
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
    for studyArea in content_list:
        name_list.append(str(studyArea['id']) + ". " + studyArea['name'] + "\n")
    update.message.reply_text("Which study area would you like to see?\nReply with /studyArea + id :)")
    update.message.reply_text("".join(name_list))


study_area_list_command_handler = CommandHandler("studyAreas", study_area_list_command)
