# This is a sample Python script.
import logging
import os

from telegram.ext import *

# api_key = os.environ['API_KEY']
import study_area_handlers.view_study_area_handler
from hostel_handlers import hostel_list_command_handler, view_hostel_handler
# RF test bot
from food_handlers import view_stall_handler, stall_list_commmand_handler
from study_area_handlers import view_study_area_handler, study_area_list_command_handler
import view_comments_handler

# RF test bot
api_key = os.environ['API_KEY']
# XC test bot
# api_key = '5097774646:AAG-O4n-xc2hmOjW0pB_evVxcgMM-EfGKjY'

updater = Updater(api_key, use_context=True)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


def start_command(update, context):
    update.message.reply_text("🔥*Welcome to RateNUS!*🔥\n\n"
                              "RateNUS was created to improve the campus living "
                              "experience of both incoming and current students. "
                              "It is an open platform that welcomes anyone's "
                              "contribution in providing accurate and useful "
                              "information about campus living/studying\n\n"
                              "🏖 To view a list of hostels: \nEnter */hostels*\n"
                              "🍱 To view a list of food stalls: \nEnter */foods*\n"
                              "📚 To view a list of study areas: \nEnter */studyareas*\n",
                              parse_mode= 'Markdown')
    chat_id = update.message.chat.id
    print("chat id: " + str(chat_id))


def handle_message(update, context):
    text = str(update.message.text)
    update.message.reply_text(text)

def main():
    # Listens for user events
    updater = Updater(api_key, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))

    dp.add_handler(hostel_list_command_handler.hostel_list_command_handler)
    dp.add_handler(view_hostel_handler.view_hostel_command_handler)

    dp.add_handler(view_comments_handler.view_comments_handler)

    dp.add_handler(stall_list_commmand_handler.stall_list_command_handler)
    dp.add_handler(view_stall_handler.view_food_command_handler)

    dp.add_handler(view_study_area_handler.view_study_area_command_handler)
    dp.add_handler(study_area_list_command_handler.study_area_list_command_handler)

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()
    updater.idle()


main()
