from flask import Flask, request
import telebot
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button1 = InlineKeyboardButton(text="Random 1-10", callback_data="randomvalue_of10")
button2 = InlineKeyboardButton(text="Random 1-100", callback_data="randomvalue_of100")

keyboard_inline = InlineKeyboardMarkup().add(button1, button2)

TOKEN = "5631307589:AAHorsEa3ZlCcAOKmdWKPCB0UWIFYrjMhbk"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)


# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "Hi Buddy, How can i help you")
#
# @bot.message_handler(commands=['help']) # help message handler
# def send_welcome(message):
#     bot.reply_to(message, 'ALPHA = FEATURES MAY NOT WORK')

@dp.message_handler(commands=["start", "help"])
async def welcome(message: types.Message):
    await message.reply("Hi hello", reply_markup=keyboard_inline)


@dp.callback_query_handler(text=["randomvalue_of10", "randomvalue_of10"])
async def random(call: types.CallbackQuery):
    if call.data == "randomvalue_of10":
        await call.message.answer("10")
    elif call.data == "randomvalue_of100":
        await call.message.answer("100")


#
# @server.route('/' + TOKEN, methods=['POST'])
# def getMessage():
#     dp.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#     return "!", 200

@server.route("/")
async def webhook():
    await bot.set_webhook(url='https://myapplicationtelegrambot.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
