from aiogram.utils import executor
from bot import dp
import handlers

async def on_startup(_):
    print('Бот запущен')

handlers.registred_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
