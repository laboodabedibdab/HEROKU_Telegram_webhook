import logging
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook
API_TOKEN = 'Ваш  токен'
WEBHOOK_HOST = 'адрес сайта'
WEBHOOK_PATH = '/path/to/api'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 3001
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
@dp.message_handler()
async def echo(message: types.Message):
    return SendMessage(message.chat.id, message.text)
async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()