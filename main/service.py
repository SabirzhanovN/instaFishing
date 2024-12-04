import telebot
import os

from dotenv import load_dotenv
load_dotenv()

token = os.getenv('TOKEN')
my_chat_id = os.getenv('CHAT_ID')
telegramBot = telebot.TeleBot(token=token)


def send_message_bot(text):
    telegramBot.send_message(chat_id=my_chat_id, text=text)

