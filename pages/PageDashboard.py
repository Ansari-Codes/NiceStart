from UI import SoftBtn, Label, Button, INIT_THEME
from utils.Storage import clearUserStorage
from utils import navigate

async def create():
    INIT_THEME()
    Label("TODO", clas="text-3xl underline text-blue-500")
    SoftBtn("LogOut", on_click=lambda: [clearUserStorage(), navigate('/')])
