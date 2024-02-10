import asyncio
import logging
from aiogram import Bot, Dispatcher
from heandlear import tets
from datetime import datetime

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6361806669:AAGN6ZWCHHw_WB1ra0DRiPm60yreIC-9Iw8")
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
dp.include_routers(tets.router)

async def main():
   await dp.start_polling(bot, mylist=[])

if __name__ == "__main__":
    asyncio.run(main())






























# @dp.message(Command("start"))
# async def command_start(message: types.Message):
#     kb = [
#         [types.KeyboardButton(text="1")],
#         [types.KeyboardButton(text="2")],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
#     await message.answer("Як подавати котлети?", reply_markup=keyboard)
    



# @dp.message(F.text.lower() == "1")
# async def with_puree(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text="oooo")


# @dp.message(F.text.lower() == "2")
# async def without_puree(message: types.Message):
#     await message.answer_dice(emoji="🎲")
    
# @dp.message(F.text.lower() == "З пюре")
# async def command_help(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id)

# @dp.message(F.text.lower() == "Без пюре")
# async def command_dice(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id)
#     await message.answer_dice(emoji="🎲")


