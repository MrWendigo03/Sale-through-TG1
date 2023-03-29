from aiogram.types import KeyboardButton

from commands import COMMANDS, COMMAND

ADD_FRAME_MATERIAL = KeyboardButton(COMMANDS["Add frame material"])
ADD_FRAME_COLOUR = KeyboardButton(COMMANDS["Add frame colour"])
ADD_CASING_MATERIAL = KeyboardButton(COMMANDS["Add casing material"])
ADD_COVER_MATERIAL = KeyboardButton(COMMANDS["Add cover material"])
ADD_COVER_COLOUR = KeyboardButton(COMMANDS["Add cover colour"])
ADD_COUNTRY_PRODUCER = KeyboardButton(COMMANDS["Add country producer"])
ADD_SPECIAL_SALES = KeyboardButton(COMMANDS["Add special sales"])
DELETE_SPECIAL_SALES = KeyboardButton(COMMANDS["Delete special sales"])
ADD_TYPE = KeyboardButton(COMMANDS["Add type"])


WATCH_ASSORTMENT = KeyboardButton(COMMAND["See assortment"])
MAKE_ORDER = KeyboardButton(COMMAND["Make order"])
SEE_SPECIALS = KeyboardButton(COMMAND["See specials"])
