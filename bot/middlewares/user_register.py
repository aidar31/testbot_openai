from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery


class RegisterCheck(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message|CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        session_maker = data['session_maker']
        user_model = data['user_model']
        async with session_maker() as session:
            async with session.begin():
                result = await session.execute(
                    select(user_model).where(user_model.user_id == event.from_user.id)
                )
                user = result.one_or_none()
                
                if user is not None:
                    pass
                else:
                    user = user_model(
                        user_id=event.from_user.id,
                        username=event.from_user.username
                    )
                    await session.merge(user)
                    if isinstance(event, Message):
                        await event.answer("Ты успешно зарегистрирован(а)!")
                    else:
                        await event.message.answer("Ты успешно зарегистрирован(а)!")
        return await handler(event, data)              