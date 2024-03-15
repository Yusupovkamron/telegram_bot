import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from maain import Database
from keyboards import menu_keyboard, menu_detail, Category_detail, men_1
load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    chat_id = message.chat.id

    check_query = f"""SELECT * FROM users WHERE chat_id = '{chat_id}'"""
    if len(Database.connect(check_query, "select")) >= 1:
        print(f"{username}")
        await message.answer(f"Hello @{username}", reply_markup=menu_keyboard)

    else:
        print(f"{first_name} start bot")
        query = f"""INSERT INTO users(first_name, last_name, user_name, chat_id) VALUES('{first_name}', '{last_name}', '{username}', '{chat_id}')"""
        print(f"{username}, {Database.connect(query, "insert")} database")
        print(f"{username}")
        await message.answer(f"Hello @{username}", reply_markup=menu_keyboard)


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

@dp.message_handler(commands=['data'])
async def select(message: types.Message):
    chat_id = message.chat.id
    query_select = f"SELECT * FROM users WHERE chat_id = '{chat_id}'"
    data = Database.connect(query_select, "select")
    print(data)
    await message.reply(f"""
        Salom @{data[0][3]}

        First Name: {data[0][1]}
        Last Name: {data[0][2]}""")
@dp.message_handler(lambda massage: massage.text == "Menyu")
async def show_menu(massage: types.Message):
    await massage.answer("Menyulardan birini tanlang", reply_markup=menu_detail)

@dp.message_handler(lambda massage: massage.text == "Category")
async def show_category(massage: types.Message):
    await massage.answer("Categorydan birini tanlang", reply_markup=Category_detail)

@dp.message_handler(lambda massage: massage.text == "menu 1")
async def show_meni_01(massage: types.Message):
    await massage.answer("Raqamlarni birini tanlang", reply_markup=men_1)


@dp.message_handler(lambda massage: massage.text == "Back")
async def back(massage: types.Message):
    await massage.answer("Menyu yoki categoryni tanlang", reply_markup=menu_keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
