from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("""
    🤖  TTS Bot haqida ;
                         

    Bu bot matnlarni ovozli formatga aylantiradi. 🎙️
                         
    📌 Foydalanish tartibi:
    
    🔹 Matn yuboring ;
    🔹 Bot uni ovozga aylantirib qaytaradi 🎧
                         
                         
    💡 Bu bot 'Sifatedu' uquv markazi tomonidan yaratilgan.
""")

