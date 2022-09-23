from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button1 = InlineKeyboardButton(text="Random 1-10", callback_data="randomvalue_of10")
button2 = InlineKeyboardButton(text="Random 1-100", callback_data="randomvalue_of100")

keyboard_inline = InlineKeyboardMarkup().add(button1, button2)

TOKEN = "5631307589:AAHorsEa3ZlCcAOKmdWKPCB0UWIFYrjMhbk"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def welcome(message: types.Message):
    await message.reply("Hi hello", reply_markup=keyboard_inline)


@dp.callback_query_handler(text=["randomvalue_of10", "randomvalue_of100"])
async def random(call: types.CallbackQuery):
    if call.data == "randomvalue_of10":
        await call.message.answer("10")
    elif call.data == "randomvalue_of100":
        await call.message.answer("100")


executor.start_polling(dp)
