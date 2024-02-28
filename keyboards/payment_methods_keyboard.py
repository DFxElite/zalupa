from aiogram import types

keyboard = types.InlineKeyboardMarkup(1)
qiwi = types.InlineKeyboardButton('💜 ЮMoney | 💳 Карта', callback_data='method_qiwi')
back = types.InlineKeyboardButton('Назад', callback_data='cancel_payment')
keyboard.add(qiwi, back)