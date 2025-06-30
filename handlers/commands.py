from aiogram.types import Message, CallbackQuery
from aiogram import Router,F
from aiogram.filters import Command,or_f
from pyexpat.errors import messages
from keyboards.reply import menu_kb
from keyboards.inline import about_kb,country_kb1,country_kb2


command_router = Router()




#старт
@command_router.message(Command('start'))
async def start_handler(message: Message):
    start_text = (
        'Привет! Помогу тебе с выбором достопримечательности в твоем путешествии. \n Выбери страну для путешествия. ✈🌏'
    )
    #отправить сообщение .answer()
    await message.answer(text=start_text, reply_markup=country_kb1)



#@command_router.message(Command('about'))
#async def about_handler(message: Message):
#    about_text = (
#        'Я предложу тебе множество классных мест для посещения в туристических городах. Жми "start"'
#    )
#    await message.answer(text = about_text)

@command_router.message(F.text.lower() == "привет")
async def say_hi(message: Message):
    await message.reply(text = 'Приветствую! 👀')


@command_router.message(F.text.lower().contains('❤'))
async def send_cute_msg(message: Message):
    cute_text = 'Спасибо за сердечко!'
    await message.answer(text=cute_text)

#Отвечаем на любой стикер
@command_router.message(F.sticker)
async def react_to_sticker(message: Message):
    await message.reply(text = 'Классный стикер! 👍')

#ответ на фото
@command_router.message(F.photo)
async def react_to_photo(m:Message):
    text_to_photo = 'Отличное фото)'
    await m.reply(text = text_to_photo)

#когда он написал спасибо и это ответ на наше соо
@command_router.message(F.reply_to_message & F.text.lower().contains('спасибо'))
async def react_to_photo(m:Message):
    await m.reply(text = 'Не за что!👌')

#Пока
@command_router.message(F.text.lower().contains('пока'))
async def say_bye(m:Message):
    await m.reply(text='До скорой встречи ❤')

@command_router.message(Command('about'))
async def about_info(message: Message):
    about_message = "Ты вызвал команду /about\nТут можешь познакомиться с ботом"
    await message.answer(text=about_message,reply_markup=about_kb)


@command_router.message(Command('menu'))
async def show_menu(message: Message):
    menu_message = 'Ты вызвал команду menu \n Выбери '
    await message.answer(text = menu_message,reply_markup=menu_kb)

@command_router.message(F.text == 'docs')
async def send_docs(message: Message):
    await message.answer(text = 'some doc info')

@command_router.message(Command('style'))
async def send_styles(message:Message):
    text = (
        "<b>bold</b> -- <strong>bold</strong>\n"
        "<i>italic</i> -- <em>italic</em>\n"
        "<u>underline</u> -- <ins>underline</ins>\n"
        "<s>strikethrough</s> -- <strike>strikethrough</strike> --  <del>strikethrough</del>\n"
        "<span class=\"tg-spoiler\">spoiler</span> -- <tg-spoiler>spoiler</tg-spoiler>\n"
        "<b>bold   <i>italic bold   <s>italic bold strikethrough "
        "<span class=\"tg-spoiler\">italic bold strikethrough spoiler</span>"
        "</s> <u>underline italic bold</u></i> bold</b>\n"
        "<a href=\"http://www.example.com/\">inline URL</a>\n"
        "<code>inline fixed-width code</code>\n"
        "<pre>pre-formatted fixed-width code block</pre>\n"
        "<pre><code class=\"language-python\">pre-formatted fixed-width code block written in the Python programming "
        "language</code></pre>"

    )
    await message.answer(text=text,parse_mode='HTML')




#@command_router.message()
#async def echo_handler(message: Message):
#   await message.answer(message.text)