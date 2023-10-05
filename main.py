from multiprocessing import freeze_support
import asyncio

from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import setup_handler
from bot import dp, start_bot

bot = Bot(token="6356405623:AAG_wfzANu298lPE18TTGDPZ-wnj7Dd-u-M")
dp = Dispatcher(storage=MemoryStorage())


router = Router(name=__name__)

@router.message()
async def message_handler(message: Message):
    await message.answer("sadsdasd")

dp.include_router(router)

async def start_bot():
    await dp.start_polling(bot)

asyncio.run(start_bot())