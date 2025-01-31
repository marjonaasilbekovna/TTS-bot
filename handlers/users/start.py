from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart
from keyboard_buttons.default.admin_keyboard import button

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text=f"Assalomu alaykum {full_name}  TTs botimizga hush kelibsiz.\nMatnni ovozga aylantirish uchun tugmani tanlang.\n\nBu bot 'Sifatedu' uquv markazi tomanidan yaratilgan.", reply_markup=button)
    except:
        await message.answer(text=f"Assalomu alaykum {full_name}  TTs botimizga hush kelibsiz.\nMatnni ovozga aylantirish uchun tugmani tanlang.\n\nBu bot 'Sifatedu' uquv markazi tomanidan yaratilgan.", reply_markup=button)

