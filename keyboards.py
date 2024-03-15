# menu_keyboard = ReplyKeyboardMarkup(resize_keyboard = True)
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("Menyu"), KeyboardButton("Category")]
], resize_keyboard=True)

menu_detail = ReplyKeyboardMarkup([
    [KeyboardButton("menu 1"), KeyboardButton("menu 2")],
    [KeyboardButton("menu 3"), KeyboardButton("menu 4")],
    [KeyboardButton("Back")]
], resize_keyboard=True)


Category_detail = ReplyKeyboardMarkup([
    [KeyboardButton("Category 1"), KeyboardButton("Category 2")],
    [KeyboardButton("Category 3"), KeyboardButton("Category 4")],
    [KeyboardButton("Back")]
], resize_keyboard=True)


men_1 = ReplyKeyboardMarkup([
    [KeyboardButton("1"), KeyboardButton("2")],
    [KeyboardButton("3"), KeyboardButton("4")],
    [KeyboardButton("Back")]
],  resize_keyboard=True)