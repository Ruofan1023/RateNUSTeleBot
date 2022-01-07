import requests
from telegram.ext import *

url = 'https://www.ratenus.cyou:8080/comment'

def view_comments(update, context):
    type = context.args[0]
    id = context.args[1]
    req_url = url + "/" + type + "/" +str(id);
    body = {
        "orderBy": "id",
        "isLowToHigh": True,
        "pageNum": 0,
        "pageSize": 100
    }
    response = requests.post(req_url, json=body)
    print(response.json())
    response_json = response.json()
    comment_list = []
    content_list = response_json['content']
    list_len = len(content_list)
    if list_len > 0:
        comment_list.append("🔥" + str(content_list[0]['targetName']) + "🔥" + "\n\n")
        for comment in content_list:
            comment_list.append("⭐ Rating: " + str(comment['rating']) + "/5.0 \n")
            comment_list.append("✏️ Comment: " + str(comment['text']) + "\n\n")
        update.message.reply_text("".join(comment_list))
    else:
        update.message.reply_text("No comments available, add one now!")



view_comments_handler = CommandHandler("comments", view_comments)