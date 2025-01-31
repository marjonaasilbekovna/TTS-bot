from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("Bu bot sizga matnlaringizni tez va oson 🔊 ovozli habarga aylantirishga yordam beradi.Bot oson va sifatli ishlaydi.")

