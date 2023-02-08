from aiogram import Router
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command, Text

from bot.logger import logger
from bot.controller import Controller


router = Router()

ADMINS = [912532345, 892021419]


@router.message(Command('subscribe'))
async def cmd_subscribe(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Подписаться", callback_data="subscribe")
        ]
    ])
    await message.answer(
        "Нажмите на кнопку, чтобы подписаться на призыв:",
        reply_markup=kb
    )



@router.message(Command('all'))
async def cmd_all(message: Message, controller: Controller):
    if message.from_user.id in ADMINS:
        rows = await controller.get_subscribers(message.chat.id)
        text = f"{message.from_user.full_name} запустил призыв!\n\n"
        index = 1
        for row in rows:
            text += f"[😶](tg://user?id={row.user_id})"
            if index < 6:
                text += " "
            else:
                text += "\n"
                index = 0
            index += 1
        await message.reply(text, parse_mode="MarkDown")
    else:
        await message.reply("Вы не администратор.")


@router.callback_query(Text('subscribe'))
async def callback_subscribe(call: CallbackQuery, controller: Controller):
    if await controller.get_user(call.from_user.id) is None:
        await controller.authorize_user(call.from_user.id, call.message.chat.id)
        await call.answer("Вы подписались на призыв.")
    else:
        await call.answer("Вы уже подписаны на призыв.")
