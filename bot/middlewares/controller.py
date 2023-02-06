from typing import Dict, Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Update
from sqlalchemy.orm import sessionmaker

from bot.db.adapter import DatabaseAdapter
from bot.controller import Controller


class ControllerMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any]
    ) -> Any:
        session_maker: sessionmaker = data.get("_session_maker")

        async with session_maker() as session:
            db = DatabaseAdapter(session)
            data["controller"] = Controller(db)
            return await handler(event, data)
        