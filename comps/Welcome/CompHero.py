from UI import Label, Card, Center, SoftButton, LinkBtn, Raw, AddSpace
from routes import ROUTES
from ENV import APP_NAME, FAVICON
from utils.Auth import isAuthenticated

def CompHero():
    with Card("w-full h-fit flex justify-center items-center border-0 sm:border-12"):
        with Center("max-w-3xl h-full gap-2 flex flex-col"):
            Label(APP_NAME + FAVICON, "text-5xl md:text-7xl lg:text-9xl font-extrabold w-full text-center")
            Label("Start your projects in a nice way!", "text-sm sm:text-lg w-full border-b-2 italic text-right")
            with Raw.RawRow("w-full justify-center items-center gap-2"):
                if not isAuthenticated():
                    LinkBtn("Sign Up", ROUTES.SIGNUP, icon="add")
                    LinkBtn("Login", ROUTES.LOGIN, icon="person")
                else:
                    LinkBtn("Dashboard", ROUTES.DASHBOARD, icon="dashboard")
                AddSpace()