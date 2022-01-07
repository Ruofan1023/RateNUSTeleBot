import requests
from telegram.ext import *

url = 'https://www.ratenus.cyou:8080/hostel'


def view_hostel_command(update, context):
    hostel_id = context.args[0]
    req_url = url + "/" + str(hostel_id)
    response = requests.get(req_url)
    response_data = response.json()

    update.message.reply_text(response_data['description'])


view_hostel_command_handler = CommandHandler("hostel", view_hostel_command)