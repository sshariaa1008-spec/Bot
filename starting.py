from aiogram.filters import CommandStart
from aiogram import F, Router
from aiogram.types import Message, FSInputFile, CallbackQuery
from sqlite3 import connect
from buttons import button, but, buying
import requests
start_router=Router()


info=connect('starria.db')
cursor=info.cursor()
a={}
@start_router.message(CommandStart())
async def begin(message: Message):
    username=message.from_user.username
    first_name=message.from_user.first_name
    last_name=message.from_user.last_name
    id=message.from_user.id
    try:
        cursor.execute("insert into star(id,username,first_name,last_name) values(?,?,?,?)", (id,username,first_name,last_name))
        info.commit()
        await message.reply (f"Hello {first_name} ({username})")
        
                            
    except:
        print('Already exists')
        await message.reply (f"Welcome back {first_name} ({username})")
    rasm=FSInputFile('Photobotkjh.jpg')
    await message.answer_photo(photo=rasm, caption="WELCOME",reply_markup=but)







# @dp.callback_query(F.data)
# async def pro(call: CallbackQuery):
#     xabar=call.data
#     await call.message.answer(xabar)

@start_router.callback_query(F.data=="Products")
async def pro(call: CallbackQuery):
    rasm=FSInputFile("Photobotkjh.jpg")
    await call.message.answer_photo(photo=rasm, caption="Available products", reply_markup=button().as_markup() )




@start_router.callback_query(F.data=="ha")
async def get(call: CallbackQuery):
        pro=a[call.from_user.id] 
        cursor.execute('''insert into savat(user_id,title,price) values(?,?,?)''', (call.from_user.id, pro['title'], pro['price']))
        info.commit()   
        await call.message.answer('Added')


@start_router.callback_query(F.data=="yoq")
async def sto(call: CallbackQuery):
    await call.message.reply(f"{call.from_user.first_name} uchun tugadi")





@start_router.callback_query(F.data)
async def find(call: CallbackQuery):
    
    xab=call.data.strip()
    print(xab)
    response=requests.get(url="https://dummyjson.com/products").json()
    for i in response['products']:
        if i['title']==xab:
            a[call.from_user.id]=i
            # print(i['images'], i['price'])
            await call.message.reply_photo(photo=f'{i['images'][0]}', caption=f'{i['title']}\n{i['price']}')
            await call.message.answer('Sotib olishni xoxlaysizmi?', reply_markup=buying)             
            break
    else:
        await call.message.reply('Topilmadi')


