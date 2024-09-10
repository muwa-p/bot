import config

import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType

# log
logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# echo bot

@dp.message_handler(content_types=["text"])
async def echo(message):
    bot.send_message(message.chat.id, message.text)

# run long-polling

if __name__ == "main":
    executor.start_polling(dp, skip_updates=False)

