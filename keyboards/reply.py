from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text='docs')]
    ],
    resize_keyboard = True
)