from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


TOKEN = "5631307589:AAHorsEa3ZlCcAOKmdWKPCB0UWIFYrjMhbk"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


def make_keyboard(button_list, call_back_function):
    buttons = []
    for button_name in button_list:
        button = InlineKeyboardButton(text=button_name, callback_data=call_back_function)
        buttons.append(button)
    keyboard_inline = InlineKeyboardMarkup().add(buttons)
    return keyboard_inline


@dp.message_handler(commands=["start", "help"])
async def welcome(message: types.Message):
    lobs = ["Telemedia", "Postpaid"]
    call_back_function = "env"
    keyboard_inline = make_keyboard(lobs, call_back_function)
    await message.reply("Hi hello Please choice the lob:- ", reply_markup=keyboard_inline)


@dp.callback_query_handler(text=["env"])
async def random(call: types.CallbackQuery):
    env = {"telemedia_env": ["PT", "SIT"]}
    call_back_function = "random"
    keyboard_inline = make_keyboard(env[str(call.message) + "_env"], call_back_function)
    await call.message.answer("please choice the env", reply_markup=keyboard_inline)


@dp.callback_query_handler(text=["random"])
async def random(call: types.CallbackQuery):
    await call.message.answer("Hkamslfa ")

# def start():
#     lobs = ["Telemedia", "Postpaid"]
#     telemedia_env = ["PT", "SIT"]
#
#     context.lob = input("Please select lob from :-  " + str(lobs))
#     context.env = input("Please select env from :-  " + str(envs))
#
#     uj_list = prop.getEnvPropValue(context.lob, 'USER_JOURNEYS', "UJ_LIST")
#
#     get_uj = input("Please select UJ from :-  " + str(uj_list))
#
#     sub_uj_list = prop.getEnvPropValue(context.lob, 'UJ_SUBSECTION', get_uj)
#
#     get_sub_uj = input("Please select SUB UJ from :-  " + str(sub_uj_list))
#
#     uj_query_variables = prop.getEnvPropValue(context.lob, 'UJ_QUERY_VARIABLES', get_sub_uj).split(",")
#     context.variables["query_name"] = uj_query_variables[0]
#     context.variables["query_variables"] = uj_query_variables[1:]
#
#     query_inputs = context.variables["query_name"]+"_input"
#
#     context.variables[query_inputs] = []
#     for query_variable in context.variables["query_variables"]:
#         context.variables[query_inputs].append(input("Please provide :-  " + query_variable))
#     get_and_validate(context, prop)

executor.start_polling(dp)
