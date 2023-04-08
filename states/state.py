from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminState(StatesGroup):
    add_frame_material = State()  # +
    add_frame_colour = State()  # +
    add_casing_material = State()  # +
    add_cover_material = State()  # +
    add_cover_colour = State()  # +
    add_country_producer = State()
    add_type = State()  # +
    add_special_sale = State()
    add_description = State()
    delete_special_sale = State()


class CustomerState(StatesGroup):  # Клиентская часть
    client_type_state = State()  # +
    client_material_frame_state = State()  # Материал каркаса +
    client_colour_material_frame_state = State()  # Цвет каркаса +
    client_material_casing_state = State()  # Материал обивки +
    client_type_material_cover_state = State()  # Материал чехла +
    client_colour_material_cover_state = State()  # Цвет чехла +
    client_country_state = State()  # +
    see_specials = State()
    see_assortment = State()
