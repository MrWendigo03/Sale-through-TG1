import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from configs import BOT_TOKEN
from filters import TrueAdmin


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
bot.admins = list(map(int, os.getenv("ADMINS_ID").split(",")))


dp.filters_factory.bind(TrueAdmin)
