from UI import Label, LinkBtn, Header, RawRow
from ENV import APP_NAME
from utils.Auth import isAuthenticated
from routes.ROUTES import LOGIN, SIGNUP, DASHBOARD

def CompHeader():
    with Header(clas="flex flex-row justify-between items-center") as header:
        Label(APP_NAME, "text-xl font-bold")
        with RawRow(clas="w-fit gap-2"):
            if isAuthenticated():
                LinkBtn('Dashboard', DASHBOARD)
            else:
                LinkBtn('Login', LOGIN)
                LinkBtn('Signup', SIGNUP)
    return header