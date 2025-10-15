from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram import F, Router

c_router=Router()





@c_router.callback_query(F.data=="Contact developer")
async def contacting(call: CallbackQuery):
    xabars=call.data
    print(xabars)
    await call.bot.send_message(chat_id=6721822487, text=f"@{call.from_user.username} dan so'rov bor")
    await call.message.answer("So'rovingiz yuborildi.")