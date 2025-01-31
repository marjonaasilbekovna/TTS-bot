from aiogram.types import Message, FSInputFile, ReplyKeyboardRemove, CallbackQuery
from aiogram.fsm.context import FSMContext
from loader import dp
from gtts import gTTS
import os
from aiogram import F
from states.help_stt import Ovoz
from keyboard_buttons.default.admin_keyboard import button
from keyboard_buttons.inline.menu import menu

@dp.message(F.text == "🔊 Ovozli habar yaratish")
async def text_to_speech(message: Message, state : FSMContext ):
    await message.reply("<b>Ovozli habarga aylantirish uchun matn kiriting!</b>",parse_mode='html', reply_markup=ReplyKeyboardRemove())
    await state.set_state(Ovoz.ovoz)

@dp.message(F.text, Ovoz.ovoz)
async def send_advert(message: Message, state: FSMContext):
    text = message.text

    waiting_message = await message.answer("⌛️")

    tts = gTTS(text, lang='en')
    audio_file = "output.mp3"
    tts.save(audio_file)

    voice = FSInputFile(audio_file)
    await message.reply_voice(voice, reply_markup=menu)

    await waiting_message.delete()

    os.remove(audio_file)

@dp.message(Ovoz.ovoz)
async def ovoz_1(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Iltimos faqat so'z kiriting ❗️")

@dp.callback_query(F.data == "orqaga_qaytish")
async def orqaga_qaytish(call: CallbackQuery, state:FSMContext):
    await state.clear()
    text = "<b>🏠 Siz bosh menudasiz</b>"
    await call.message.answer(text, parse_mode='html', reply_markup=button)

@dp.message()
async def ignore_messages(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state != Ovoz.ovoz:
        await message.answer("<b>Iltimos, tugmalardan foydalaning ❗️</b>", parse_mode='html')
