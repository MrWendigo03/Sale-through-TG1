from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from bot import dp
from commands import COMMAND
from state import CustomerState


@dp.message_handler(Text(COMMAND["Make order"]))
async def add_cover_material(message: Message):
    await message.answer("Хорошо, тип мебели вы хотите заказать?")
    await CustomerState.client_type_state.set()

@dp.message_handler(state=CustomerState.client_type_state)
async def add_frame_col(message: Message, state: FSMContext):
    await state.update_data(client_type_state=message.text)
    await message.answer("Хорошо, а из какого материала хотите ваш заказ?")
    await CustomerState.client_material_frame_state.set()

@dp.message_handler(state=CustomerState.client_material_frame_state)
async def add_material_frame(message: Message, state: FSMContext):
    await state.update_data(client_material_frame_state=message.text)
    await message.answer("Хорошо, а какого цвета каркас?")
    await CustomerState.client_colour_material_frame_state.set()

@dp.message_handler(state=CustomerState.client_colour_material_frame_state)
async def add_colour_material_frame(message: Message, state: FSMContext):
    await state.update_data(client_colour_material_frame_state=message.text)
    await message.answer("Хорошо, из какого материала хотите сделать обивку?")
    await CustomerState.client_material_casing_state.set()

@dp.message_handler(state=CustomerState.client_material_casing_state)
async def add_casing_material_type(message: Message, state: FSMContext):
    await state.update_data(client_material_casing_state=message.text)
    await message.answer("Хорошо, из какого материала хотите сделать покрытие?")
    await CustomerState.client_type_material_cover_state.set()

@dp.message_handler(state=CustomerState.client_type_material_cover_state)
async def add_cover_material_type(message: Message, state: FSMContext):
    await state.update_data(client_type_material_cover_state=message.text)
    await message.answer("Хорошо, какого цвета должен быть материал?")
    await CustomerState.client_colour_material_cover_state.set()

@dp.message_handler(state=CustomerState.client_colour_material_cover_state)
async def add_cover_material_colour(message: Message, state: FSMContext):
    await state.update_data(client_colour_material_cover_state=message.text)
    await message.answer("Хорошо, из какой страны должен быть материал?")
    await CustomerState.client_country_state.set()

@dp.message_handler(state=CustomerState.client_country_state)
async def add_country(message: Message, state: FSMContext):
    await state.update_data(client_country_state=message.text)
    await message.answer("Хорошо, ваш заказ принят.")
async def send_order(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(data)

@dp.message_handler(Text(COMMAND["See assortment"]))
async def watch_content(message: Message):
    await message.answer("Хорошо")
    await CustomerState.see_assortment.set()

@dp.message_handler(state=CustomerState.see_assortment)
async def watch_assort(message: Message, state: FSMContext):
    await state.update_data(see_assortment=message.text)
    await message.answer("На данный момент, эта функция дорабатывается.")
    await state.finish()

@dp.message_handler(Text(COMMAND["See specials"]))
async def watch_content(message: Message):
    await message.answer("")
    await CustomerState.see_specials.set()

@dp.message_handler(state=CustomerState.see_specials)
async def watch_specials(message: Message, state: FSMContext):
    await state.update_data(see_specials=message.text)
    await message.answer("На данный момент, эта функция дорабатывается.")
