import config
from telegram.ext import Updater, CommandHandler
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token=config.TOKEN, request_kwargs=config.REQUEST_KWARGS)
dispatcher = updater.dispatcher

podcasts = {'Some':'link', 'Et Leffans. Episode 1.':'bit.ly/090090'}  # for debug.


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def search(bot, update, args):
    title = ''
    for arg in args:
        title += arg + ' '
    title = title[:-1]
    substr = ''
    for k in podcasts.keys():
        if title in k:
            substr += k + podcasts[k] + '\n'
    bot.send_message(chat_id=update.message.chat_id, text="Here's the variants:\n" + substr)
    print("Here's the variants:\n" + substr)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
search_handler = CommandHandler(['s', 'search'], search, pass_args=True)
dispatcher.add_handler(search_handler)
updater.start_polling()
