import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler
import requests

def inline_search(update, context):
    query = update.inline_query.query

    if not query:
        return

    results = []
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/search_messages?chat_id={CHAT_ID}&query={query}'
    response = requests.get(url)
    posts = response.json()['result']

    for post in posts:
        message_text = post['message']['text']
        title = f"Post by {post['message']['from']['username']}"
        results.append(
            InlineQueryResultArticle(
                id=post['message_id'],
                title=title,
                input_message_content=InputTextMessageContent(message_text)
            )
        )

    update.inline_query.answer(results)

if name == 'main':
    # Replace with your bot token and chat ID
    BOT_TOKEN = '5837194490:AAHz2PMk4mIyRlLjLcwacSAIIM04WjEMD8I'
    CHAT_ID = '-1001856402326'

    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    inline_search_handler = InlineQueryHandler(inline_search)
    dispatcher.add_handler(inline_search_handler)
    updater.start_polling()
    updater.idle()
