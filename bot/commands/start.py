from aiogram import Router, types
from aiogram.filters import CommandStart


start_router = Router(name="start")

@start_router.message(CommandStart())
async def start_handler(msg: types.Message):
    return await msg.answer("Привет! Я ChatGPT Бот. Я готов ответить на ваши вопросы и вести с вами беседу. Просто отправьте мне сообщение, и я постараюсь вам помочь. Для начала беседы просто напишите что-то интересное!")