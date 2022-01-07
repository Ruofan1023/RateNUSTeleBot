import requests
from telegram.ext import *

url = 'https://www.ratenus.cyou:8080/stall'


def view_food_command(update, context):
    link = '[here](https://ratenus.com)'
    print(str(len(context.args)) + " " + str(type(context.args[0])))
    if len(context.args) == 1:
        hostel_id = context.args[0]
        req_url = url + "/" + str(hostel_id)
        response = requests.get(req_url)
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
        update.message.reply_text("To view a food place's info, enter /food with the restaurant id")


view_food_command_handler = CommandHandler("food", view_food_command)
