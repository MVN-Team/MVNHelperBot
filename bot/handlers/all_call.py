from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.logger import logger


router = Router()


@router.message(Command('all'))
async def call_all(message: Message):
    ...
