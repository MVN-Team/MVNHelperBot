from sqlalchemy.ext.asyncio import AsyncSession, AsyncSessionTransaction
from sqlalchemy import select, update, delete, insert

from bot.db.models import Subscriber


class DatabaseAdapter:
    def __init__(self, session: AsyncSession):
        self.session = session

    def transaction(self) -> AsyncSessionTransaction:
        return self.session.begin()

    async def authorize_user(self, user_id: int, chat_id: int):
        await self.session.execute(
            insert(Subscriber).values(user_id=user_id, chat_id=chat_id)
        )
        
    async def get_user(self, user_id: int):
        stmt = select(Subscriber).where(Subscriber.user_id == user_id)
        return (await self.session.execute(stmt)).fetchone()
        
    async def get_subscribers(self, chat_id: int):
        stmt = select(Subscriber).where(Subscriber.chat_id == chat_id)
        return (await self.session.execute(stmt)).scalars().all()
    