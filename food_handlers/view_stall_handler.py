import re

import requests
from telegram.ext import *

import constants

url = 'https://www.ratenus.cyou:8080/stall'


def view_food_command(update, context):
    pattern = re.compile(r'^[-+]?[0-9]+$')
    link = '[here](https://ratenus.com)'
    if len(context.args) == 1 and re.fullmatch(pattern, context.args[0]):
        hostel_id = context.args[0]
        req_url = url + "/" + str(hostel_id)
        response = requests.get(req_url)
        if response.status_code == 200:
            response_data = response.json()
            text = "🏖️ {name}\n📍 {location}\n⭐ {rating} ({commentCount} {review})\n\n{description}\n" \
                .format(name=response_data['name'], location=response_data['location'],
                        rating=str(response_data['rating']) + " / 5.0" if response_data['rating'] >= 0 else "No rating",
                        commentCount=response_data['commentCount'],
                        review="review" if response_data['commentCount'] <= 1 else "reviews",
                        description=response_data['description'])
            update.message.reply_text(text, parse_mode='Markdown')
            stall_name = response_data['name']
            stall_id = str(response_data['id'])
            photo = response_data['imageUrl'][0]
            context.bot.sendPhoto(chat_id=update.message.chat.id, photo=photo)
            update.message.reply_text("To view the rating & reviews for " +
                                      stall_name + ", please reply with /comments food " + stall_id +
                                      "\. For more information, please visit our website " + link + "\.",
                                      parse_mode='MarkDownV2')
        else:
            update.message.reply_text(constants.not_found_message)
    else:
        update.message.reply_text("To view a food place's info, enter /food with the restaurant id")


view_food_command_handler = CommandHandler("food", view_food_command)
