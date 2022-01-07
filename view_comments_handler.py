import requests
from telegram.ext import *

url = 'https://www.ratenus.cyou:8080/comment'


def view_comments(update, context):
    if len(context.args) != 2:
        update.message.reply_text("Invalid command, please try again!")
    else:
        link = '[here](https://ratenus.com)'
        comment_type = context.args[0]
        if comment_type == "stall":
            update.message.reply_text("Invalid command, please try again!")
        else:
            if comment_type == "food":
                comment_type = "stall"
            elif comment_type == "studyarea":
                comment_type = "studyArea"
            id = context.args[1]
            req_url = url + "/" + comment_type + "/" + str(id);
            body = {
                "orderBy": "id",
                "isLowToHigh": True,
                "pageNum": 0,
                "pageSize": 100
            }
            response = requests.post(req_url, json=body)
            if response.status_code == 200:
                response_json = response.json()
                comment_list = []
                content_list = response_json['content']
                list_len = len(content_list)
                if list_len > 0:
                    comment_list.append("🔥" + str(content_list[0]['targetName']) + "🔥" + "\n\n")
                    for comment in content_list:
                        comment_list.append("⭐ Rating: " + str(comment['rating']) + " / 5.0 \n")
                        comment_list.append("✏️ Comment: " + str(comment['text']) + "\n\n")
                    update.message.reply_text("".join(comment_list))
                else:
                    update.message.reply_text("No comments available, try adding one " + link, parse_mode='MarkDownV2')
            else:
                update.message.reply_text("Invalid command, please try again!")


view_comments_handler = CommandHandler("comments", view_comments)
