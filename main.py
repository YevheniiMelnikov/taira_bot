import logging
import asyncio
import aioschedule
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from other import main_menu

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token='5517267462:AAGQnx8i4mRf8jCp5lRQKTu7mUrOe2pNwNA')
dp = Dispatcher(bot, storage=storage)

chat_id = -1001704309768  # фактический id
test_id = -1001685640249  # тестовый чат


@dp.message_handler()
async def good_morning():
    await bot.send_message(chat_id, 'Доброе утро! Вы завтракали сегодня? 🙂', reply_markup=main_menu)
   
    
@dp.message_handler()
async def good_day():
    await bot.send_message(chat_id, 'Добрый день! Вы обедали сегодня? 🙂', reply_markup=main_menu)


@dp.message_handler()
async def good_night():
    await bot.send_message(chat_id, 'Добрый вечер! Вы ужинали сегодня? 🙂', reply_markup=main_menu)
    
    
@dp.message_handler()
async def drink_water():
    await bot.send_message(chat_id, 'Не забывай пить воду 💧')
    

async def scheduler():
    aioschedule.every().day.at("07:00").do(good_morning)
    aioschedule.every().day.at("10:00").do(drink_water)
    aioschedule.every().day.at("13:00").do(drink_water)
    aioschedule.every().day.at("14:00").do(good_day)
    aioschedule.every().day.at("15:00").do(drink_water)
    aioschedule.every().day.at("19:00").do(drink_water)
    aioschedule.every().day.at("18:00").do(good_night)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)

