from aiogram import Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.dispatcher.dispatcher import Dispatcher

bot = Bot(token="6356405623:AAG_wfzANu298lPE18TTGDPZ-wnj7Dd-u-M")
dp = Dispatcher(storage=MemoryStorage())


def start_bot():
    dp.start_polling(bot, skip_updates=True,)# on_startup=app_startup, on_shutdown=app_shutdown)