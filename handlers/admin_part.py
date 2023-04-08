from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from bot import dp
from KeyBoard.commands import COMMANDS
from configs import Session
from filters.filters import TrueAdmin
from models import FrameInfo, CasingMaterial, CoverInfo, CountryInfo, Sales
from states.state import AdminState

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
    async with state.proxy() as data:
        frame_material = data["add_frame_material"]
    await state.reset_state(True)
    await state.finish()
    async with Session() as session:
        frame_mat = FrameInfo(name_frame_material=frame_material)
        session.add(frame_mat)
        session.commit()
    await message.reply("Материал добавлен.")

@dp.message_handler(Text(COMMANDS["Add frame colour"]), TrueAdmin())
async def add_frame_colour(message: Message):
    await message.reply("Хорошо, какой цвет каркасного материала вы хотите добавить?")
    await AdminState.add_frame_material.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_frame_material)
async def add_frame_col(message: Message, state: FSMContext):
    await state.update_data(add_frame_colour=message.text)
    async with state.proxy() as data:
        frame_colour = data["add_frame_colour"]
    await state.reset_state(True)
    await state.finish()
    async with Session() as session:
        frame_col = FrameInfo(name_frame_colour=frame_colour)
        session.add(frame_col)
        session.commit()
    await message.reply("Цвет материала добавлено.")

@dp.message_handler(Text(COMMANDS["Add casing material"]), TrueAdmin())
async def add_casing_material(message: Message):
    await message.reply("Хорошо, какой обивочный материал вы хотите добавить?")
    await AdminState.add_casing_material.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_casing_material)
async def add_frame_col(message: Message, state: FSMContext):
    await state.update_data(add_casing_material=message.text)
    async with state.proxy() as data:
        casing_material = data["add_casing_material"]
    await state.reset_state(True)
    await state.finish()
    async with Session() as session:
        case_mat = CasingMaterial(name_casing_material=casing_material)
        session.add(case_mat)
        session.commit()
    await message.reply("Обивка добавлена.")

@dp.message_handler(Text(COMMANDS["Add cover material"]), TrueAdmin())
async def add_cover_material(message: Message):
    await message.reply("Хорошо, какой материал для покрытия вы хотите добавить?")
    await AdminState.add_cover_material.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_cover_material)
async def add_cover_mat(message: Message, state: FSMContext):
    await state.update_data(add_cover_material=message.text)
    async with state.proxy() as data:
        cover_material = data["add_cover_material"]
    await state.reset_state(True)
    await state.finish()
    async with Session() as session:
        frame_col = CoverInfo(name_cover_material=cover_material)
        session.add(frame_col)
        session.commit()
    await message.reply("Покровочный материал добавлен.")

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
    await state.finish()
    with Session() as session:
        cover_col = CoverInfo(name_cover_colour=cover_colour)
        cover_col.commit()
        session.commit()
    await message.reply("Цвет покровочного материала добавлен.")

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
    await state.finish()
    with Session() as session:
        cover_col = CountryInfo(country_name=country_producer)
        cover_col.commit()
        session.commit()
    await message.reply("Страна производитель добавлена.")

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
    await state.finish()
    with Session()as session:
        cover_col = CountryInfo(country_name=type1)
        cover_col.commit()
        session.commit()
    await message.reply("Тип добавлен.")

@dp.message_handler(Text(COMMANDS["Add special sales"]), TrueAdmin())
async def add_type(message: Message):
    await message.reply("Хорошо, какую акцию вы хотите добавить?")
    await AdminState.add_special_sale.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_special_sale)
async def add_type_to_des(message: Message, state: FSMContext):
    await state.update_data(add_special_sale=message.text)
    await message.reply("Хорошо, добавьте описание скидки")
    await AdminState.add_description.set()

@dp.message_handler(TrueAdmin(), state=AdminState.add_description)
async def add_description(message: Message, state: FSMContext):
    await state.update_data(add_description=message.text)
    async with state.proxy() as data:
        name_of_sale = data["name_of_sale"]
        description = data["description"]
    await state.reset_state(True)
    await state.finish()
    if message not in Sales:
        with Session()as session:
            spec_sale = Sales(name_of_sale=name_of_sale)
            descr = Sales(description=description)
            spec_sale.commit()
            descr.commit()
            session.commit()
    else:
        await message.answer("Акции уже существует!")
    await message.reply("Скидка/акция добавлена.")

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
    await state.finish()
    if message in Sales:
        with Session()as session:
            spec_sale = Sales(country_name=delete_sale)
            spec_sale.delete()
            session.delete()
    else:
        await message.answer("Нет такой акции!")
    await message.reply("Скидка/акция удалена.")
