import requests
import os
import logging
from dotenv import load_dotenv
from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler


load_dotenv()
BOT_TOKEN = str(os.getenv('TOKEN'))
print(BOT_TOKEN)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

URL = 'https://api.thecatapi.com/v1/images/search'

bot = Bot(token=BOT_TOKEN)
updater = Updater(token=BOT_TOKEN)
my_chat_id = '211399878'
text = 'Муррррр!!!'
# bot.send_message(my_chat_id, text)


def get_new_image() -> str:
    try:
        response = requests.get(URL).json()
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url).json()
    
    random_cat = response[0].get('url')
    return random_cat


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, я KittyForFriendsBot!'
    )


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([
                ['/newcat'],
            ], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}! Посмотри какого котика я тебе нашел.',
        reply_markup=buttons
    )

    context.bot.send_photo(
        chat.id,
        get_new_image()
    )


def main():
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()