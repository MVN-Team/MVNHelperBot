import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.handlers import setup_routers
from bot.config import Settings
from bot.logger import logger


async def main():
    config = Settings()

    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    router = setup_routers()
    dp.include_router(router)


    kwargs = {
        'config': config
    }


    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), **kwargs)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")