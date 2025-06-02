from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

API_TOKEN = 'YOUR_BOT_TOKEN'  # Замените на ваш токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: Message):
    await message.answer("Бот онлайн. Используйте /player")

@dp.message_handler(commands=['player'])
async def player_cmd(message: Message):
    await message.answer("В разработке")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
