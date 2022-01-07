# This is a sample Python script.
from telegram import InlineQueryResultArticle, InputTextMessageContent, Bot
import logging
from telegram.ext import *
from telegram.utils import helpers

# api_key = os.environ['API_KEY']
import hostel_list_command_handler
import view_hostel_handler
# RF test bot
api_key = '5066015679:AAFJzkzf6dN513gH06zU_uVYRlKsS22vqlY'
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
                              "🏖 To view a list of hostels: \nEnter */hostel*\n"
                              "🍱 To view a list of food stalls: \nEnter */food*\n"
                              "📚 To view a list of study areas: \nEnter */studyArea*\n",
                              parse_mode= 'Markdown')
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
