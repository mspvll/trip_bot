from idlelib.undo import Command
from mailbox import Message

from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline import country_kb1, country_kb2, russia_kb,usa_kb,italy_kb,spain_kb,china_kb,brasil_kb
from aiogram.types import InputMediaPhoto


callback_router = Router()
@callback_router.callback_query(F.data.in_(['prev','next']))
async def country_callback(callback: CallbackQuery):
    if callback.data == "next":
        await callback.message.edit_text(' Выбери страну для путешествия.', reply_markup=country_kb2)
    else:
        await callback.message.edit_text(' Выбери страну для путешествия.', reply_markup=country_kb1)
    await callback.answer()

#страны
@callback_router.callback_query(F.data == 'rus')
async def second_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Выбери город 👇🏻",
                                  reply_markup=russia_kb)

@callback_router.callback_query(F.data == 'usa')
async def second_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Выбери город 👇🏻",
                                  reply_markup=usa_kb)
@callback_router.callback_query(F.data == 'italy')
async def second_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Выбери город 👇🏻",
                                  reply_markup=italy_kb)
@callback_router.callback_query(F.data == 'spain')
async def second_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Выбери город 👇🏻",
                                  reply_markup=spain_kb)
@callback_router.callback_query(F.data == 'china')
async def second_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Выбери город 👇🏻",
                                  reply_markup=china_kb)
@callback_router.callback_query(F.data == 'brasil')
async def second_chapter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Выбери город 👇🏻",
                                  reply_markup=brasil_kb)

#города

@callback_router.callback_query(F.data == 'moscow')
async def send_album(callback: CallbackQuery):
    media = [
        InputMediaPhoto(media="https://www.multitour.ru/files/out/topplace-moscow/Moskovskii_universitet/Moskovskii_universitet_3.jpg"),
        InputMediaPhoto(media='https://ekskursii-v-moskve.ru/wp-content/uploads/2020/12/ekskusrii-po-moskve.jpg'),
        InputMediaPhoto(media='https://www.classicalmusicnews.ru/wp-content/uploads/2025/01/bolshoj-teatr4.jpg')
    ]
    await callback.answer("Загружаем")
    await callback.message.answer_media_group(media)
    await callback.message.edit_text(text='1️⃣МГУ \n ️2️⃣Красная площадь \n 3️⃣Большой театр')

@callback_router.callback_query(F.data == 'spb')
async def send_album(callback: CallbackQuery):
    await callback.answer("Загружаем")
    await callback.message.answer_photo(photo = 'https://www.multitour.ru/files/out/topplace-spb/Petergof/1.jpg', caption='1️⃣ <b>Петергоф </b>\nОн был основан в 1710 году в качестве загородной резиденции правителей. Для функционирования всех фонтанов был проложен отдельный водопровод, протяженность которого 40 км. Петр Первый часто останавливался здесь.', parse_mode='HTML')
    await callback.message.answer_photo(photo = 'https://www.multitour.ru/files/out/topplace-spb/Isaakievskii-sobor/1.jpg', caption='2️⃣ <b>Исаакиевский собор </b> \nВнутри собор отделан драгоценными породами камней, великолепными ручными росписями, фресками. Интерьерную работу выполняли почти 17 лет, а общие затраты составили 23 миллиона рублей. ', parse_mode='HTML')
    await callback.message.answer_photo(photo = 'https://www.multitour.ru/files/out/topplace-spb/Petergof/1.jpg', caption='3️⃣ <b>Дворцовая площадь </b> \nЭто место считается первым исторически сложившимся архитектурным ансамблем. На дворцовой площади находится Зимний дворец, который ранее был императорским. ', parse_mode='HTML')
    await callback.message.answer(text='Смог ли я помочь тебе?')

@callback_router.callback_query(F.data == 'murmansk')
async def send_album(callback: CallbackQuery):
    await callback.answer("Загружаем")
    await callback.message.answer_photo(photo = 'https://cdn.tripster.ru/thumbs2/b3616590-1baa-11ec-8121-46f338c2ea01.384x289.jpg', caption='1️⃣ <b>Ледокол «Ленин» </b>\n Является первым в мире надводным судном с ядерной силовой установкой.В настоящее время на корабле работает музей. Это единственный объект культурного наследия федерального значения в Мурманске.', parse_mode='HTML')
    await callback.message.answer_photo(photo = 'https://cdn.tripster.ru/thumbs2/d3da836a-1cc0-11ee-b8ac-c6401ab82aad.384x289.jpg', caption='2️⃣ <b>Монумент «Алёша» </b> \nПамятник является центром мемориала, посвящённого воинам, освободившим Заполярье от фашистов.', parse_mode='HTML')
    await callback.message.answer_photo(photo = 'https://cdn.tripster.ru/thumbs2/de6c9a3e-1baf-11ec-931a-66788eb007b3.384x289.jpg', caption='3️⃣ <b>Мыс Абрам </b> \nНа мысу расположен небольшой микрорайон города Мурманска. Путешественников привлекает красота и уединённость здешних мест. ', parse_mode='HTML')
    await callback.message.answer(text='Смог ли я помочь тебе?')



@callback_router.callback_query(F.data == 'vegas')
async def send_album(callback: CallbackQuery):
    await callback.answer("Загружаем")
    await callback.message.answer_photo(photo = 'https://russiantouramerica.com/wp-content/uploads/2018/05/Fontany-Belladzhio-free-55.png', caption='1️⃣ <b>Фонтаны Белладжио</b>\nсегодня Фонтаны Белладжио, без всякого сомнения, являются главной достопримечательностью Лас-Вегаса, очаровывая своей грациозностью и красотой всех, без исключения, гостей города.', parse_mode='HTML')
    await callback.message.answer_photo(photo = 'https://russiantouramerica.com/wp-content/uploads/2018/05/Zapovednik-Springs-free-1.png', caption='2️⃣ <b>Заповедник Спрингс </b> \nЗаповедник Спрингс имеет внушительную площадь, более 70 гектар и раскинулся на побережье водохранилища, которое обеспечивает водой весь город. ', parse_mode='HTML')
    await callback.message.answer(text='Смог ли я помочь тебе?')

@callback_router.callback_query(F.data == 'ny')
async def send_album(callback: CallbackQuery):
    await callback.answer("Загружаем")
    await callback.message.answer_photo(photo = 'https://images.squarespace-cdn.com/content/v1/563a5fb2e4b0710808c31f27/1511649577117-6XIGA4EC5805L90JDBZT/%D1%82%D0%B0%D0%B8%CC%86%D0%BC%D1%81+%D1%81%D0%BA%D0%B2%D0%B5%D1%80.jpg?format=2500w', caption='1️⃣ <b>Таймс Сквер</b>\nTimes square - сердце индустрии развлечений города. Все бродвейский шоу и театры расположены вокруг этой площади.', parse_mode='HTML')
    await callback.message.answer_photo(photo = 'https://images.squarespace-cdn.com/content/v1/563a5fb2e4b0710808c31f27/1511721885832-IAUDJ38P7WG1K90K7Q4P/%D1%84%D0%BB%D1%8D%D1%82_%D0%B0%D0%B9%D1%80%D0%BE%D0%BD_%D0%B1%D0%B8%D0%BB%D0%B4%D0%B8%D0%BD%D0%B3_%D0%BD%D1%8C%D1%8E%D0%B9%D0%BE%D1%80%D0%BA%D0%B3%D0%B8%D0%B4.jpg?format=2500w', caption='2️⃣ <b> Флэтайрон билдинг </b> \nЗдание Флэтайрон было построено в 1902 году и стало первым небоскребом к северу от 14-й улицы. Архитектором был Даниел Хадсон Бёрнем из Чикаго, и Флэтайрон - стало его единственным зданием в Нью-Йорке.', parse_mode='HTML')
    await callback.message.answer(text='Смог ли я помочь тебе?')

@callback_router.callback_query(F.data == 'la')
async def send_album(callback: CallbackQuery):
    await callback.answer("Загружаем")
    await callback.message.answer_photo(photo = 'https://russiantouramerica.com/wp-content/uploads/2018/05/Gollivudskaja-Alleja-Slavy-7.png', caption='1️⃣ <b>Аллея Славы</b>\nВсего здесь насчитывается более 2,6 тысяч звезд и ежегодно десятки миллионов человек проходят по Аллее Славы, чтобы увидеть имена своих кумиров.', parse_mode='HTML')
    await callback.message.answer_photo(photo = 'https://russiantouramerica.com/wp-content/uploads/2024/01/Disnejlend-Los-Andzheles-1.png', caption='2️⃣ <b>Диснейленд </b> \n Диснейленд Лос-Анджелеса, это первый, детский, развлекательный парк Диснея открытый где либо в мире!', parse_mode='HTML')
    await callback.message.answer(text='Смог ли я помочь тебе?')

@callback_router.callback_query(F.data == 'rome')
async def send_album(callback: CallbackQuery):
    await callback.answer("Загружаем")
    await callback.message.answer_photo(photo = 'https://cdn.tripster.ru/thumbs2/710d0f7a-2f3b-11eb-b198-4245fbb1d7a4.384x289.jpg', caption='1️⃣ <b>Пантеон</b>\n Он был построен за несколько веков до нашей эры и представлял собой храм всех греческих богов. Неоднократно горел и перестраивался. Теперешний вид здание приобрело во втором столетии нашей эры.', parse_mode='HTML')
    await callback.message.answer_photo(photo = 'https://cdn.tripster.ru/thumbs2/710d0f7a-2f3b-11eb-b198-4245fbb1d7a4.384x289.jpg', caption='2️⃣ <b>Колизей</b> \n Само здание Колизея построено для проведения боёв гладиаторов ещё в I столетии нашей эры. В XIV веке сильное землетрясение разрушило южную часть Колизея. Лишь в XIX веке уцелевшую часть архитектурного памятника восстановили. ', parse_mode='HTML')
    await callback.message.answer(text='Смог ли я помочь тебе?')

@callback_router.callback_query(F.data == 'venice')
async def send_album(callback: CallbackQuery):
    await callback.answer("Загружаем")
    await callback.message.answer_photo(photo = 'https://7d9e88a8-f178-4098-bea5-48d960920605.selcdn.net/a83bdf28-ac2d-4994-a549-636b6d23fb64/-/format/jpeg/-/quality/lighter/-/stretch/off/-/resize/1900x/', caption='1️⃣ <b>Гранд-канал</b>\nБудучи главной улицей, он пересекает весь город от вокзала до здания таможенной службы. Необычным это пространство делает отсутствие берегов и привычных набережных.', parse_mode='HTML')
    await callback.message.answer_photo(photo = 'https://italy4.me/wp-content/uploads/2022/07/Basilica-di-San-Marco-Venice.jpg', caption='2️⃣ <b>Собор Святого Марка </b> \n Этот храм — одна из самых красивых построек в Европе. В его помещениях до сих можно увидеть привезенные из Византии сокровища. Одним из них является реликварий Животворящего Креста.', parse_mode='HTML')
    await callback.message.answer(text='Смог ли я помочь тебе?')

@callback_router.callback_query(F.data == 'barselona')
async def send_album(callback: CallbackQuery):
    await callback.answer("Загружаем")
    await callback.message.answer_photo(photo = 'https://cdn.tripster.ru/thumbs2/b8022482-8dd5-11ee-af0d-b2207d87956d.384x289.jpg', caption='1️⃣ <b>Кафедральный собор Барселоны/b>\n Строительство собора началось в XIII веке и продолжалось в течение нескольких веков. В его облике были использованы различные архитектурные стили, что придало ему уникальный и изысканный вид. Барселонский собор приковывает взгляд изящными готическими линиями, высокими башнями и ошеломляющей росписью на стенах и витражах.', parse_mode='HTML')
    await callback.message.answer_photo(photo = 'https://cdn.tripster.ru/thumbs2/d6ac7d1e-2344-11eb-8783-76da2c94d373.384x289.jpg', caption='2️⃣ <b>Саграда Фамилия </b> \n Создание храма началось ещё в XIX веке, — гениальный архитектор Антонио Гауди принял участие в работе над проектом. Собор Саграда-Фамилия пропитан глубоким религиозным смыслом. Его название — «Святое Семейство» — указывает на то, что он посвящён Христу, его родителям и апостолам.', parse_mode='HTML')
    await callback.message.answer(text='Смог ли я помочь тебе?')

@callback_router.callback_query(F.data == 'madrid')
async def send_album(callback: CallbackQuery):
    await callback.answer("Загружаем")
    await callback.message.answer_photo(photo = 'https://avatars.mds.yandex.net/get-vertis-journal/3934100/4.jpg_1712032501755/1200x1200', caption='1️⃣ <b>Пласа-Майор</b>\n Прямоугольная площадь, на которой пересекаются девять городских улиц, выполнена в едином стиле испанского барокко. У окружающих «Пласа-Майор» зданий почти 400 балконов.', parse_mode='HTML')
    await callback.message.answer_photo(photo = 'https://avatars.mds.yandex.net/get-vertis-journal/4212087/9_florian-wehde-WBGjg0DsO_g-unsplash.jpg_1712032722929/1200x1200', caption='2️⃣ <b>Бульвар Гран-Виа</b> \n Он протянулся через центр города от улицы Алькалы до площади Испании. Здесь соседствуют ювелирные и модные бутики, сувенирные лавки и гипермаркеты, роскошные отели и театры, рестораны и кинозалы. ', parse_mode='HTML')
    await callback.message.answer(text='Смог ли я помочь тебе?')

@callback_router.callback_query(F.data == 'pekin')
async def send_album(callback: CallbackQuery):
    await callback.answer("Загружаем")
    await callback.message.answer_photo(photo = 'https://cdn.tripster.ru/thumbs2/861d4f4a-50c8-11ee-89f3-dec745f69ab5.384x289.jpg', caption='1️⃣ <b>Великая Китайская стена/b>\n В общей сложности на возведение масштабного сооружения понадобилось более 2000 лет и около двух миллионов человек, многие из которых погибли во время стройки из-за нечеловеческих условий труда. Кроме защиты от набегов врагов, Великая Китайская стена служит для обозначения границы.', parse_mode='HTML')
    await callback.message.answer_photo(photo = 'https://cdn.tripster.ru/thumbs2/062996b2-524a-11ee-8374-b65df4c6b373.384x289.jpg', caption='2️⃣ <b>Юнхэгун</b> \n В 1694 году в Пекине появился дворец с храмом, изначально предназначавшийся для жизни дворцовых евнухов. В 1723 году комплекс перешёл к принцу Иньчжэню и стал его резиденцией. Он передал часть сооружений ламаистскому монастырю, которому дали простое название «Юнхэгун», то есть храм Ламы. ', parse_mode='HTML')
    await callback.message.answer(text='Смог ли я помочь тебе?')

@callback_router.callback_query(F.data == 'shanhai')
async def send_album(callback: CallbackQuery):
    await callback.answer("Загружаем")
    await callback.message.answer_photo(photo = 'https://avatars.mds.yandex.net/get-vertis-journal/4220003/3.jpg_1710313849625/1200x1200', caption='1️⃣ <b>Набережная Вайтань</b>\nОдно из самых интересных мест города, откуда открывается вид на деловой район Пудун, где расположены всемирный финансовый центр Шанхая, генеральное консульство Российской Федерации, а ещё — телебашня «Восточная жемчужина», занимающая пятое место в мире по высоте', parse_mode='HTML')
    await callback.message.answer_photo(photo = 'https://avatars.mds.yandex.net/get-vertis-journal/4220003/5.jpg_1710314024373/1200x1200', caption='2️⃣ <b>Сад Юйюань</b> \n Это настоящий традиционный китайский сад, созданный ещё во времена династии Мин — строительство начали в 1559 году.', parse_mode='HTML')
    await callback.message.answer(text='Смог ли я помочь тебе?')

@callback_router.callback_query(F.data == 'rio')
async def send_album(callback: CallbackQuery):
    await callback.answer("Загружаем")
    await callback.message.answer_photo(photo = 'https://cdn.radiosputnik.ru/images/152127/71/1521277132_765:0:2813:2048_1920x0_80_0_0_83018015653b0513a5813090ecb36d40.jpg', caption='1️⃣ <b>Статуя Христа-Искупителя</b>\n статуя Иисуса Христа в стиле ар-деко, расположенная на вершине горы Корковаду в Рио-де-Жанейро. Является символом города и Бразилии в целом.', parse_mode='HTML')
    await callback.message.answer_photo(photo = 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/02/69/65/ef/praia-de-copacabana-ao.jpg?w=900&h=500&s=1', caption='2️⃣ <b>Morro da Urca</b> ', parse_mode='HTML')
    await callback.message.answer(text='Смог ли я помочь тебе?')