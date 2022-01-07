import requests
from telegram.ext import *

url = 'https://www.ratenus.cyou:8080/studyarea'


def view_study_area_command(update, context):
    link = '[here](https://ratenus.com)'
    print(str(len(context.args)) + " " + str(type(context.args[0])))
    if len(context.args) == 1:
        hostel_id = context.args[0]
        req_url = url + "/" + str(hostel_id)
        response = requests.get(req_url)
        response_data = response.json()
        print(response_data)
        text = "🏖️ {name}\n📍 {location}\n⭐ {rating} ({commentCount} {review})" \
            .format(name=response_data['name'], location=response_data['location'],
                    rating=str(response_data['rating']) + " / 5.0" if response_data['rating'] >= 0 else "No rating",
                    commentCount=response_data['commentCount'],
                    review="review" if response_data['commentCount'] <= 1 else "reviews")
        update.message.reply_text(text, parse_mode='Markdown')
        study_area_name = response_data['name']
        study_area_id = str(response_data['id'])
        photo = response_data['imageUrl'][0]
        context.bot.sendPhoto(chat_id=update.message.chat.id, photo=photo)
        update.message.reply_text("To view the rating & reviews for " +
                                  study_area_name + ", please reply with /comments studyArea " + study_area_id +
                                  "\. For more information, please visit our website " + link + "\.",
                                  parse_mode='MarkDownV2')
    else:
        update.message.reply_text("To view a study area's info, enter /studyArea with the study area id")


view_study_area_command_handler = CommandHandler("studyArea", view_study_area_command)
