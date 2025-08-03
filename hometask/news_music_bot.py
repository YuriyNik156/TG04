import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN4
import tg_buttons as tg_b

bot = Bot(token=TOKEN4)
dp = Dispatcher()

# При отправке команды /start бот будет показывать меню с кнопками "Привет" и "Пока".
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Выберите кнопку:", reply_markup=tg_b.buttons)

@dp.message(F.text == "Привет") # Обработка кнопки "Привет"
async def hello(message: Message):
    await message.answer (f"Привет, {message.from_user.first_name}!")

@dp.message(F.text == "До свидания") # Обработка кнопки "До свидания"
async def buy(message: Message):
    await message.answer (f"До свидания, {message.from_user.first_name}!")

# При отправке команды /links бот будет показывать инлайн-кнопки с URL-ссылками.
@dp.message(Command('links'))
async def links(message: Message):
    await message.answer("Выберите ссылку", reply_markup=tg_b.inline_buttons)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())