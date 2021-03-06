import requests
from telegram.ext import *

url = 'https://www.ratenus.cyou:8080/studyarea'


def study_area_list_command(update, context):
    body = {
        "orderBy": "id",
        "isLowToHigh": True,
        "pageNum": 0,
        "pageSize": 100
    }
    response = requests.post(url, json=body)
    response_json = response.json()
    name_list = []
    print(response_json)
    content_list = response_json['content']
    for studyArea in content_list:
        name_list.append(str(studyArea['id']) + ". " + studyArea['name'] + "\n")
    update.message.reply_text("Which study area would you like to see?\nReply with /studyarea + id :)")
    update.message.reply_text("".join(name_list))


study_area_list_command_handler = CommandHandler("studyareas", study_area_list_command)
