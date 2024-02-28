from aiogram import types

def make_keyboard(url: str, type: str, pref = ''):
    keyboard = types.InlineKeyboardMarkup(1)
    link = types.InlineKeyboardButton('💳 Перейти к оплате', callback_data='XYU')
    check = types.InlineKeyboardButton('🔄 Проверить оплату', callback_data='ZA')
    cancel = types.InlineKeyboardButton('❌ Отменить', callback_data='cancel_payment')
    keyboard.add(link, check, cancel)
    return keyboard