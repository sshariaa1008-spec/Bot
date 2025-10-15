from aiogram import F, Router
from aiogram.types import Message, FSInputFile, CallbackQuery
from sqlite3 import connect
info=connect('starria.db')
cursor=info.cursor()



s_router=Router()


@s_router.callback_query(F.data=="Savat")
async def sav(call: CallbackQuery):
    id=call.from_user.id
    h=0
    cursor.execute(""" select savat.title, savat.price
                   FROM savat
                   JOIN star ON savat.user_id=star.id  where savat.user_id=?
                   """, (id,))
    await call.message.answer(f'{call.from_user.username} sotib olgan narsalar:')
    for i in cursor.fetchall():
        h=h+i[1]
        await call.message.answer(f'{i[0]},{i[1]}')
    await call.message.answer(f"Umumiy narx: {h}")