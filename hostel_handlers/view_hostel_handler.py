import requests
from telegram.ext import *

url = 'https://www.ratenus.cyou:8080/hostel'


def view_hostel_command(update, context):
    print(str(len(context.args)) + " " + str(type(context.args[0])))
    if len(context.args) == 1:
        hostel_id = context.args[0]
        req_url = url + "/" + str(hostel_id)
        response = requests.get(req_url)
        response_data = response.json()
        print(response_data)
        text = "⭐️ {name}\n📍 {location}\n{description}" \
            .format(name=response_data['name'], location=response_data['location'],
                    description=response_data['description'])
        update.message.reply_text(text, parse_mode='Markdown')
    else:
        update.message.reply_text("To view a hostel's info, enter /hostel with the hostel id")



view_hostel_command_handler = CommandHandler("hostel", view_hostel_command)
