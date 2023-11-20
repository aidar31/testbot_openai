from aiogram import Router, types
from aiogram.filters import Command

help_router = Router(name="help")


@help_router.message(Command("help"))
async def help_handler(msg: types.Message):
    return await msg.answer('Okay, im help!')