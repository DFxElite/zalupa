from loader import dp, bot
from aiogram import types


@dp.callback_query_handler(text='ZA')
async def check_payment(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, '<b>❌ Вы не совершили оплату!</b>')
    
    
@dp.callback_query_handler(text='XYU')
async def succes_payment(callback: types.CallbackQuery):
    text = '''
<b>💳 Реквизиты для оплаты: 
    💎 Карта МИР: <code>2204 1201 1592 3753</code>
    🌐 Кошелёк ЮMoney: <code>4100 1185 4600 4649</code>
    
💠 После оплаты нажмите "<i>🔄 Проверить оплату.</i>"</b>
    '''
    await bot.send_message(callback.from_user.id, text)