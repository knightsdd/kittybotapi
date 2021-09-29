import requests
from telegram import Bot
from pprint import pprint


BOT_TOKEN = '2016456927:AAH53QEcjZUVRrv1AAiwlzQypyZIxGGbE4o'
MY_CHAT_ID = '211399878'

bot = Bot(token=BOT_TOKEN)

URL = 'https://api.thecatapi.com/v1/images/search'

response = requests.get(URL).json()

pprint(response)

print(type(response))

print(len(response))

print(type(response[0]))

random_cat_url = response[0].get('url')

chat_id = MY_CHAT_ID

bot.send_photo(chat_id, random_cat_url)
# text = 'Вам телеграмма!'
# Отправка сообщения
# bot.send_message(chat_id, text)
# Отправка изображения
# bot.send_photo(chat_id, URL)
