from aiogram.types import Message

from KeyBoard.Keyboard import administrator_keys_list, user_keys_list
from loaders import dp
from filters.filters import TrueAdmin


@dp.message_handler(TrueAdmin(), commands=['start'])
async def hello_admin(message: Message):
    await message.answer("Привет! Администратор, Ваши доступные комманды", reply_markup=administrator_keys_list)


@dp.message_handler(commands=['start'])
async def hello_user(message: Message):
    await message.answer(
        "Приветствую, Заказчик, я делаю на заказ мебель. Выберете тип мебели, который вы хотите заказать. На данный "
        "момент я могу собрать для вас: шифонеры, столы, стулья, кухонные шкафы - с доступной цветовой гаммой",
        reply_markup=user_keys_list)
