from nicegui import app


def isAuthenticated():
    return app.storage.user.get("auth", False)
