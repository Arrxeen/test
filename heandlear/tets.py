from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from key.for_questions import get_yes_no_kb
from random import randint

router = Router()  # [1]

@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Налити?",
        reply_markup=get_yes_no_kb()
    )

@router.message(F.text.lower() == "так")
async def answer_yes(message: Message, mylist: list[int]):
    a=randint(100,250)

    mylist.append(a)
    await message.answer(
        f"Ви випили {a}мл.",
        
    )

@router.message(F.text.lower() == "ні")
async def answer_no(message: Message):
    await message.answer(
        "Жаль...",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text.lower()== "скільки випив")
async def len_list(message: Message, mylist: list[int]):
    a=0
    for i in range(len(mylist)):
        litr = int(mylist[i])
        a += litr  
    await message.answer(f"Скільки ви випили кофе: {a}мл.")
    