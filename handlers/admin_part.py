from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from bot import dp
from commands import COMMANDS
from filters import TrueAdmin
from state import AdminState

dp.filters_factory.bind(TrueAdmin)


@dp.message_handler(Text(COMMANDS["Add frame material"]), TrueAdmin())
async def add_frame_material(message: Message):
    await message.reply("Хорошо, какой каркасный материал вы хотите добавить?")
    await AdminState.add_frame_material.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_frame_material)
async def add_frame_mat(message: Message, state: FSMContext):
    await state.update_data(add_frame_material=message.text)
    await message.reply("Добавлено.")
    await state.finish()

@dp.message_handler(Text(COMMANDS["Add frame colour"]), TrueAdmin())
async def add_frame_colour(message: Message):
    await message.reply("Хорошо, какой цвет каркасного материала вы хотите добавить?")
    await AdminState.add_frame_material.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_frame_material)
async def add_frame_col(message: Message, state: FSMContext):
    await state.update_data(add_frame_colour=message.text)
    await message.reply("Добавлено.")
    await state.finish()

@dp.message_handler(Text(COMMANDS["Add casing material"]), TrueAdmin())
async def add_casing_material(message: Message):
    await message.reply("Хорошо, какой обивочный материал вы хотите добавить?")
    await AdminState.add_casing_material.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_casing_material)
async def add_frame_col(message: Message, state: FSMContext):
    await state.update_data(add_casing_material=message.text)
    await message.reply("Добавлено.")
    await state.finish()

@dp.message_handler(Text(COMMANDS["Add cover material"]), TrueAdmin())
async def add_cover_material(message: Message):
    await message.reply("Хорошо, какой материал для покрытия вы хотите добавить?")
    await AdminState.add_cover_material.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_cover_material)
async def add_frame_col(message: Message, state: FSMContext):
    await state.update_data(add_cover_material=message.text)
    await message.reply("Добавлено.")
    await state.finish()

@dp.message_handler(Text(COMMANDS["Add cover colour"]), TrueAdmin())
async def add_cover_colour(message: Message):
    await message.reply("Хорошо, какой цвет покровочного материала вы хотите добавить?")
    await AdminState.add_cover_colour.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_cover_colour)
async def add_frame_col(message: Message, state: FSMContext):
    await state.update_data(add_cover_colour=message.text)
    await message.reply("Добавлено.")
    await state.finish()

@dp.message_handler(Text(COMMANDS["Add country producer"]), TrueAdmin())
async def add_cover_colour(message: Message):
    await message.reply("Хорошо, в какой стране произведён материал?")
    await AdminState.add_cover_colour.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_cover_colour)
async def add_frame_col(message: Message, state: FSMContext):
    await state.update_data(add_cover_colour=message.text)
    await message.reply("Добавлено.")
    await state.finish()

@dp.message_handler(Text(COMMANDS["Add type"]), TrueAdmin())
async def add_type(message: Message):
    await message.reply("Хорошо, какой тип мебели вы хотите добавить?")
    await AdminState.add_type.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_type)
async def add_type(message: Message, state: FSMContext):
    await state.update_data(add_type=message.text)
    await message.reply("Добавлено.")
    await state.finish()

@dp.message_handler(Text(COMMANDS["Add special sales"]), TrueAdmin())
async def add_type(message: Message):
    await message.reply("Хорошо, какую акцию вы хотите добавить?")
    await AdminState.add_type.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_type)
async def add_type(message: Message, state: FSMContext):
    await state.update_data(add_type=message.text)
    await message.reply("Добавлено.")
    await state.finish()

@dp.message_handler(Text(COMMANDS["Delete special sales"]), TrueAdmin())
async def add_type(message: Message):
    await message.reply("Хорошо, какую акцию вы хотите добавить?")
    await AdminState.add_type.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_type)
async def add_type(message: Message, state: FSMContext):
    await state.update_data(add_type=message.text)
    await message.reply("Удалено.")
    await state.finish()
