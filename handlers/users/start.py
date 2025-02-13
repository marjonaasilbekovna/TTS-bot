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
        await message.answer(text=f"""
Assalomu alaykum! 👋

Hurmatli {full_name}  ❤️                          

Men matnni ovozga aylantiruvchi botman. 🎙️
Menga matn yuboring, men esa uni siz uchun ovozli qilib beraman! 🔊

📌 Foydalanish:
1️⃣ Oddiy matn yuboring.
2️⃣ Men uni ovozga aylantirib, sizga yuboraman. 🎧

Qo‘shimcha yordam kerak bo‘lsa,  '/help'  tugmasidan foydalaning. 🚀


""", reply_markup=button)
    except:
        await message.answer(text=f"""
Assalomu alaykum! 👋

Hurmatli {full_name}  ❤️                          

Men matnni ovozga aylantiruvchi botman. 🎙️
Menga matn yuboring, men esa uni siz uchun ovozli qilib beraman! 🔊

📌 Foydalanish:
1️⃣ Oddiy matn yuboring.
2️⃣ Men uni ovozga aylantirib, sizga yuboraman. 🎧

Qo‘shimcha yordam kerak bo‘lsa,  '/help'  tugmasidan foydalaning. 🚀


""", reply_markup=button)
