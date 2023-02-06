from aiogram import Dispatcher

from bot.middlewares import (
    controller,
)


def setup_middlewares(dp: Dispatcher) -> None:
    dp.update.middleware(controller.ControllerMiddleware())
    