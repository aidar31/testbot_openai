from aiogram import Router, types
from aiogram.filters import CommandStart

from openai import OpenAI

from mics import start_chat_gpt


gpt_router = Router(name="gpt_router")



@gpt_router.message()
async def gpt_handler(msg: types.Message, openai_client: OpenAI):
    messages = []
    loading_info = await msg.answer("Thinking...")
    text_answer = start_chat_gpt(openai_client, msg.text, messages)
    await msg.answer(text_answer)
    await msg.delete(msg.chat.id, loading_info.message_id)