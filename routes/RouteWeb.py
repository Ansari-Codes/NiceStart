from .ROUTES import MAIN, DASHBOARD
from nicegui.ui import page
from pages.PageWelcome import create as create_welcome

@page(MAIN)
async def render_main():
    await create_welcome()

@page(DASHBOARD)
def render_dashboard():
    pass
