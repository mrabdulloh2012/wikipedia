from aiogram import Dispatcher, Bot , filters, types, F
import asyncio
import wikipedia

bot = Bot(token="7345735234:AAHzGUVM5hP_0ZTc12DuCcw3l19OQqaZeVo")
dp = Dispatcher(bot = bot)
wikipedia.set_lang('uz')


orders = []


@dp.message(filters.Command("Start"))
async def start_function(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}")
    
        
@dp.message(F.text)
async def start_function(message: types.Message):
    text = wikipedia.summary(message.text)
    await message.reply(text)
    
    
@dp.message(F.data == "lavash")
async def lavash(message: types.Message):
    orders.clear()
    await message.answer("Lavash 25000")
    
       
   
async def main():
    await dp.start_polling(bot)
    
    
    
if __name__== '__main__':
    asyncio.run(main())