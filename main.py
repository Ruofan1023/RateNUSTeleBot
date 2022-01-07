# This is a sample Python script.
from telegram import InlineQueryResultArticle, InputTextMessageContent, Bot
import logging
from telegram.ext import *
from telegram.utils import helpers

# api_key = os.environ['API_KEY']
import hostel_list_command_handler
import view_hostel_handler

api_key = '5066015679:AAFJzkzf6dN513gH06zU_uVYRlKsS22vqlY'
updater = Updater(api_key, use_context=True)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
HOSTELS_LINK = 'hostels-link'

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


def start_command(update, context):
    url = helpers.create_deep_linked_url(context.bot.username, HOSTELS_LINK)
    text = "Feel free to tell your friends about it:\n\n" + url
    update.message.reply_text(text)
    # update.message.reply_text("*Welcome to RateNUS!*\n"
    #                           "🏖"
    #                           "Type 'hostel', 'food' or 'studyArea' to view NUS facilities" + "🚨",
    #                           parse_mode='Markdown')
    chat_id = update.message.chat.id
    print("chat id: " + str(chat_id))


def handle_message(update, context):
    text = str(update.message.text)
    update.message.reply_text(text)


def view_hostel_list_command(update, context):
    update.message.reply_text("Test hostels")


def view_food_list_command(update, context):
    update.message.reply_text("Test food")


def view_study_area_list_command(update, context):
    update.message.reply_text("Test study areas")


def main():
    # Listens for user events
    updater = Updater(api_key, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("hostels", hostel_list_command_handler.hostel_list_command))
    dp.add_handler(view_hostel_handler.view_hostel_command_handler)
    dp.add_handler(CommandHandler("food", view_food_list_command))
    dp.add_handler(CommandHandler("studyArea", view_study_area_list_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()
    updater.idle()


main()
