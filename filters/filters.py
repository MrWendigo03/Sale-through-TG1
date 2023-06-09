from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message


class TrueAdmin(BoundFilter):

    async def check(self, message: Message) -> bool:
        return message.from_user.id in message.bot.admins
