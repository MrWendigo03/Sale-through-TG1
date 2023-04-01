from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from bot import dp
from commands import COMMANDS
from filters import TrueAdmin
from state import AdminState

dp.filters_factory.bind(TrueAdmin)
@dp.message_handler(commands=['cancel'], state='*')
async def cancel(message: Message, state: FSMContext):
    if not await state.get_state() is None:
        await message.reply("Отменено!")
        await state.finish()


@dp.message_handler(Text(COMMANDS["Add frame material"]), TrueAdmin())
async def add_frame_material(message: Message):
    await message.reply("Хорошо, какой каркасный материал вы хотите добавить?")
    await AdminState.add_frame_material.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_frame_material)
async def add_frame_mat(message: Message, state: FSMContext):
    await state.update_data(add_frame_material=message.text)
    await message.reply("Добавлено.")
    async with state.proxy() as data:
        frame_material = data["add_frame_material"]
    await state.reset_state(True)
    await state.finish()

@dp.message_handler(Text(COMMANDS["Add frame colour"]), TrueAdmin())
async def add_frame_colour(message: Message):
    await message.reply("Хорошо, какой цвет каркасного материала вы хотите добавить?")
    await AdminState.add_frame_material.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_frame_material)
async def add_frame_col(message: Message, state: FSMContext):
    await state.update_data(add_frame_colour=message.text)
    await message.reply("Добавлено.")
    async with state.proxy() as data:
        frame_colour = data["add_frame_colour"]
    await state.reset_state(True)
    await state.finish()

@dp.message_handler(Text(COMMANDS["Add casing material"]), TrueAdmin())
async def add_casing_material(message: Message):
    await message.reply("Хорошо, какой обивочный материал вы хотите добавить?")
    await AdminState.add_casing_material.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_casing_material)
async def add_frame_col(message: Message, state: FSMContext):
    await state.update_data(add_casing_material=message.text)
    await message.reply("Добавлено.")
    async with state.proxy() as data:
        casing_material = data["add_casing_material"]
    await state.reset_state(True)
    await state.finish()

@dp.message_handler(Text(COMMANDS["Add cover material"]), TrueAdmin())
async def add_cover_material(message: Message):
    await message.reply("Хорошо, какой материал для покрытия вы хотите добавить?")
    await AdminState.add_cover_material.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_cover_material)
async def add_frame_col(message: Message, state: FSMContext):
    await state.update_data(add_cover_material=message.text)
    async with state.proxy() as data:
        cover_material = data["add_cover_material"]
    await state.reset_state(True)
    await message.reply("Добавлено.")
    await state.finish()

@dp.message_handler(Text(COMMANDS["Add cover colour"]), TrueAdmin())
async def add_cover_colour(message: Message):
    await message.reply("Хорошо, какой цвет покровочного материала вы хотите добавить?")
    await AdminState.add_cover_colour.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_cover_colour)
async def add_frame_col(message: Message, state: FSMContext):
    await state.update_data(add_cover_colour=message.text)
    async with state.proxy() as data:
        cover_colour = data["add_cover_colour"]
    await state.reset_state(True)
    await message.reply("Добавлено.")
    await state.finish()

@dp.message_handler(Text(COMMANDS["Add country producer"]), TrueAdmin())
async def add_cover_colour(message: Message):
    await message.reply("Хорошо, в какой стране произведён материал?")
    await AdminState.add_cover_colour.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_cover_colour)
async def add_frame_col(message: Message, state: FSMContext):
    await state.update_data(add_cover_colour=message.text)
    async with state.proxy() as data:
        country_producer = data["add_country_producer"]
    await state.reset_state(True)
    await message.reply("Добавлено.")
    await state.finish()

@dp.message_handler(Text(COMMANDS["Add type"]), TrueAdmin())
async def add_type(message: Message):
    await message.reply("Хорошо, какой тип мебели вы хотите добавить?")
    await AdminState.add_type.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_type)
async def add_type(message: Message, state: FSMContext):
    await state.update_data(add_type=message.text)
    async with state.proxy() as data:
        type1 = data["add_type"]
    await state.reset_state(True)
    await message.reply("Добавлено.")
    await state.finish()

@dp.message_handler(Text(COMMANDS["Add special sales"]), TrueAdmin())
async def add_type(message: Message):
    await message.reply("Хорошо, какую акцию вы хотите добавить?")
    await AdminState.add_type.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_type)
async def add_type(message: Message, state: FSMContext):
    await state.update_data(add_type=message.text)
    async with state.proxy() as data:
        special_sale = data["Add_special_sales"]
    await state.reset_state(True)
    await message.reply("Добавлено.")
    await state.finish()

@dp.message_handler(Text(COMMANDS["Delete special sales"]), TrueAdmin())
async def add_type(message: Message):
    await message.reply("Хорошо, какую акцию вы хотите удалить?")
    await AdminState.add_type.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_type)
async def add_type(message: Message, state: FSMContext):
    await state.update_data(add_type=message.text)
    async with state.proxy() as data:
        delete_sale = data["delete_special_sales"]
    await state.reset_state(True)
    await message.reply("Удалено.")
    await state.finish()
