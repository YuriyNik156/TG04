from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message


buttons = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=f"Привет")],
    [KeyboardButton(text=f"До свидания")]
], resize_keyboard=True)