import asyncio
from aiogram import Bot, Dispatcher
from antispam import AntiFloodMiddleware
from handlers.commands import command_router
from config import TOKEN
from handlers.callback import callback_router
from aiogram.fsm.storage.memory import MemoryStorage
from states import fsm_router
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot,storage=storage)
dp.include_router(command_router)
dp.include_router(callback_router)
dp.include_router(fsm_router)
dp.message.middleware(AntiFloodMiddleware())
dp.callback_query.middleware(AntiFloodMiddleware())




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
