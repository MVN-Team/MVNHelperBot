import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.config import Settings


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    
    config = Settings()

    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    # Handlers and Middlewares


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