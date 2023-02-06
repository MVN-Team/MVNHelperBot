from bot.db.adapter import DatabaseAdapter
from bot.db.models import Subscriber


class Controller:
    def __init__(self, db: DatabaseAdapter):
        self.db = db

    async def authorize_user(self, user_id: int, chat_id: int) -> None:
        async with self.db.transaction():
            await self.db.authorize_user(user_id, chat_id)
        
    async def get_user(self, user_id: int):
        async with self.db.transaction():
            return await self.db.get_user(user_id)    
        
    async def get_subscribers(self, chat_id: int):
        async with self.db.transaction():
            return await self.db.get_subscribers(chat_id)
    