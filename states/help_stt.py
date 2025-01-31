from aiogram.fsm.state import State, StatesGroup

class Help(StatesGroup):
    help = State()


class Ovoz(StatesGroup):
    ovoz = State()