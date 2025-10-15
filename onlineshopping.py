import logging
import asyncio
from aiogram import Dispatcher, Bot, F
from Bot.contacting import c_router
from Bot.savat import s_router
from Bot.starting import start_router






BOT_token="bot_token"
dp=Dispatcher()
bot=Bot(token=BOT_token)
dp.include_router(s_router)
dp.include_router(c_router)
dp.include_router(start_router)






async def testing():
    await dp.start_polling(bot)



if __name__=='__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(testing())
    except:
        print('Done')