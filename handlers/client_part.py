from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from bot import dp
from commands import COMMAND
from state import CustomerState


@dp.message_handler(Text(COMMAND["Make order"]))
async def add_cover_material(message: Message):
    await message.reply("Хорошо, тип мебели вы хотите заказать?")
    await CustomerState.client_type_state.set()

@dp.message_handler(state=CustomerState.client_type_state)
async def add_frame_col(message: Message, state: FSMContext):
    await state.update_data(client_type_state=message.text)
    await message.reply("Хорошо, а из какого материала хотите ваш заказ?")
    await CustomerState.client_material_frame_state.set()

@dp.message_handler(state=CustomerState.client_material_frame_state)
async def add_material_frame(message: Message, state: FSMContext):
    await state.update_data(client_material_frame_state=message.text)
    await message.reply("Хорошо, а какого цвета каркас?")
    await CustomerState.client_colour_material_frame_state.set()

@dp.message_handler(state=CustomerState.client_colour_material_frame_state)
async def add_colour_material_frame(message: Message, state: FSMContext):
    await state.update_data(client_colour_material_frame_state=message.text)
    await message.reply("Хорошо, из какого материала хотите сделать обивку?")
    await CustomerState.client_type_material_cover_state.set()


