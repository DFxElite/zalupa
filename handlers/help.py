from loader import dp
from aiogram import types

@dp.message_handler(text='👨🏼‍🔧 Тех. поддержка 👨🏼‍🔧')
async def help(message: types.Message):
    username = 'vpodiezdedum_101'
    keyboard = types.InlineKeyboardMarkup()
    button_acc = types.InlineKeyboardButton(text='💞 Перейти', url=f't.me/{username}', callback_data='help')
    keyboard.add(button_acc)
    await message.answer('🍓 Техническая поддержка 👇', reply_markup=keyboard)
    await message.answer_sticker('CAACAgIAAxkBAAEC3R9hNjNUj-nang5taLVR7eGvkDXcjQACOAsAAk7kmUsysUfS2U-M0CAE')