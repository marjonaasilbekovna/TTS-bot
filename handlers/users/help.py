from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("⚙️ Buyruqlar \nBotdan foydalanish uchun avval '/start' - tugmasini bosing. Keyin esa '🔊 Ovozli habar yaratish' tugmasini bosing va matningizni yozib yuboring. Bot siz yozgan matningizni ovozga aylantirib beradi.\n\n'/about' - Bot haqida qisqacha ma'lumot.\n'/bot_admin' - bot admini malumotlari.\n'/xabar' - bot adminiga mrojaat uchun.")
