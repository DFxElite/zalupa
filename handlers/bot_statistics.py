from loader import dp
from aiogram import types

@dp.message_handler(text='🌐 Статистика 🌐')
async def stats(message: types.Message):
    await message.answer('<b>🔎 Всего было поисков сливов: 22393</b>\n<b>✅ Приобрели товар: 9932</b>\n<b>📩 Сообщений отправлено ботом: 10231</b>')
    await message.answer_sticker('CAACAgIAAxkBAAEC3R1hNjNKTzLh2La_N-VGNv8VlqRsFQACSQIAAladvQoqlwydCFMhDiAE')