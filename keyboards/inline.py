from  aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
#объект кнопки и конструктор
about_kb = InlineKeyboardMarkup(
    inline_keyboard= [
        [InlineKeyboardButton(text='Github', url ='https://github.com/mspvll/trip_bot'), InlineKeyboardButton(text='Документация', url = 'docs.aiogram.dev')]
    ]
)

country_kb1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Россия', callback_data='rus')],[InlineKeyboardButton(text='США',callback_data='usa')], [InlineKeyboardButton(text='Италия',callback_data='italy')],
        [InlineKeyboardButton(text='⏩', callback_data = 'next')]

    ]
)

yes_no_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Да', callback_data='yes')],[InlineKeyboardButton(text='Нет',callback_data='no')]
    ]
)

country_kb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Испания',callback_data='spain')],[InlineKeyboardButton(text='Китай',callback_data='china')], [InlineKeyboardButton(text='Бразилия',callback_data='brasil')],
        [InlineKeyboardButton(text='⏪',callback_data = 'prev')]

    ]
)

russia_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Москва', callback_data='moscow')],
        [InlineKeyboardButton(text='Санкт-Петербург', callback_data='spb')],
        [InlineKeyboardButton(text='Мурманск', callback_data='murmansk')],
        [InlineKeyboardButton(text='⏪',callback_data = 'prev')]


    ]
)

usa_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Нью-Йорк', callback_data='ny')],
        [InlineKeyboardButton(text='Лас-Вегас', callback_data='vegas')],
        [InlineKeyboardButton(text='Лос-Анджелес', callback_data='la')],
        [InlineKeyboardButton(text='⏪',callback_data = 'prev')]


    ]
)
italy_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рим', callback_data='rome')],
        [InlineKeyboardButton(text='Венеция', callback_data='venice')],
        [InlineKeyboardButton(text='⏪',callback_data = 'prev')]

    ]
)
spain_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Барселона', callback_data='barselona')],
        [InlineKeyboardButton(text='Мадрид', callback_data='madrid')],
        [InlineKeyboardButton(text='⏪',callback_data = 'prev')]

    ]
)
china_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Пекин', callback_data='pekin')],
        [InlineKeyboardButton(text='Шанхай', callback_data='shanhai')],
        [InlineKeyboardButton(text='⏪',callback_data = 'prev')]

    ]
)
brasil_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рио-де-Жанейро', callback_data='rio')],
        [InlineKeyboardButton(text='⏪',callback_data = 'prev')]

    ]
)