from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

buttons = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=f"Привет")],
    [KeyboardButton(text=f"До свидания")]
], resize_keyboard=True)

inline_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url="https://dzen.ru/news")],
    [InlineKeyboardButton(text="Музыка", url="https://music.yandex.ru/")],
    [InlineKeyboardButton(text="Видео", url="https://www.youtube.com/")]
])
