from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bottoms import ADD_FRAME_MATERIAL, ADD_FRAME_COLOUR, ADD_CASING_MATERIAL, ADD_TYPE, ADD_COVER_COLOUR
from bottoms import ADD_COVER_MATERIAL, ADD_SPECIAL_SALES, DELETE_SPECIAL_SALES, ADD_COUNTRY_PRODUCER
from bottoms import WATCH_ASSORTMENT, MAKE_ORDER, SEE_SPECIALS

administrator_keys_list = ReplyKeyboardMarkup([
    [ADD_FRAME_MATERIAL, ADD_FRAME_COLOUR, ADD_CASING_MATERIAL],
    [ADD_COVER_MATERIAL, ADD_COVER_COLOUR, ADD_TYPE],
    [ADD_COUNTRY_PRODUCER, ADD_SPECIAL_SALES, DELETE_SPECIAL_SALES]
], resize_keyboard=True)

user_keys_list = ReplyKeyboardMarkup([
    [WATCH_ASSORTMENT, MAKE_ORDER, SEE_SPECIALS]
], resize_keyboard=True)
