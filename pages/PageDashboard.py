from UI import SoftButton, Button, INIT_THEME
from utils.Storage import clearUserStorage
from utils import navigate

async def create():
    INIT_THEME()
    SoftButton("LogOut", on_click=lambda: [clearUserStorage(), navigate('/')])
    SoftButton("Test", on_click=lambda: print("Testing"))
    Button("Test")
