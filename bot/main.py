import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.config import Settings
from bot.logger import logger
from bot.handlers import setup_routers
from bot.middlewares import setup_middlewares
from bot.db import create_session_maker, create_engine


async def main():
    config = Settings()

    engine = create_engine(config.db_url)
    session_maker = create_session_maker(engine)

    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    router = setup_routers()
    dp.include_router(router)
    setup_middlewares(dp)


    kwargs = {
        'config': config,
        '_session_maker': session_maker,
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