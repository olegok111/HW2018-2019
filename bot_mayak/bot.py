#coding: utf-8
import config
from telegram.ext import Updater, CommandHandler
import logging
import parser_prg as parser
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

WITH_PROXY = True  # You need to change this variable to True if you want to start the bot with a proxy, which is configured in config.py.
if WITH_PROXY:
    updater = Updater(token=config.TOKEN, request_kwargs=config.REQUEST_KWARGS)
else:
    updater = Updater(token=config.TOKEN)
dispatcher = updater.dispatcher

unnamed_count = 0
podcasts = {}
links_textfile = open('links.txt', mode='r', encoding='utf8')
links_lines = links_textfile.readlines()
for link_line in links_lines:
    podcast_title = link_line[:link_line.find('http')]
    podcast_link = link_line[link_line.find('http'):]
    if podcast_title == ' ':
        unnamed_count += 1
        podcasts['Без имени ' + str(unnamed_count) + ' '] = podcast_link
    else:
        podcasts[podcast_title] = podcast_link
links_textfile.close()


def start(bot, update):
    txt = "Начнём!\n Введите команду '/s запрос' или '/search запрос', чтобы начать поиск." + \
        "\nВведите команду '/u' или '/update', чтобы обновить список подкастов."
    bot.send_message(chat_id=update.message.chat_id, text=txt)

def search(bot, update, args):
    try:
        if podcasts == {}:
            bot.send_message(chat_id=update.message.chat_id, text="Идёт получение списка подкастов. Это займёт около 5 минут.")
            parser.main()
        title = ''
        for arg in args:
            title += arg + ' '
        title = title[:-1]
        substr = ''
        search_results = []
        for k in podcasts.keys():
            if title in k:
                search_results.append(k + podcasts[k])
        search_results.sort()
        for res in search_results:
            substr += res + '\n'
        bot.send_message(chat_id=update.message.chat_id, text="Результаты поиска:\n" + substr)
    except:
        bot.send_message(chat_id=update.message.chat_id, text="Введите запрос.")

def podcast_list_update(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Идёт обновление списка подкастов. Это займёт около 5 минут.")
    parser.main()
    bot.send_message(chat_id=update.message.chat_id, text="Обновление завершено!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
search_handler = CommandHandler(['s', 'search'], search, pass_args=True)
dispatcher.add_handler(search_handler)
update_handler = CommandHandler(['u', 'update'], podcast_list_update)
dispatcher.add_handler(update_handler)
updater.start_polling()
