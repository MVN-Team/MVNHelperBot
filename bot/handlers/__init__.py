from aiogram import Router

from bot.handlers import (
    all_call,
)


def setup_routers() -> Router:
    router = Router()
    
    router.include_router(all_call.router)
    
    return router
