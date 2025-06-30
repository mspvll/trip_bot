from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database import select_cost

fsm_router = Router()




class Form(StatesGroup):
    budget = State()

@fsm_router.message(Command('budget'))
async def cmd_budget(message: Message, state: FSMContext):
    await state.set_state(Form.budget)
    await message.answer('Каков ваш бюджет в рублях?')

@fsm_router.message(Form.budget)
async def procces_budget(message: Message,state:FSMContext):
    await state.update_data(budget = message.text)
    data = await state.get_data()
    budget = message.text
    budget_list = select_cost(budget)
    list1 = []
    for city,cost in budget_list:
        list1.append(city)
    if len(list1) == 0:
        await message.answer(text='К сожалению, у меня нет предложений за такую сумму 😥')
    else:
        await message.answer(text=f'Вам подойдут туры в такие города, как:\n<b>{str('\n'.join(str(x) for x in list1))}</b> \nПодробнее о городах можешь узнать, нажав на кнопку <b>"start"</b>', parse_mode='HTML')
    await state.clear()