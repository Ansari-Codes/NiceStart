from .Model import Model, Required
from lib.dbQuery import Query
from datetime import datetime

class Auth(Model):
    def __init__(self):
        super().__init__()
    
    def create(self, obj: dict):
        name = obj.get("name")
        email = obj.get("email")
        password = obj.get("password")
        if not name: raise Required("Name")
        if not email: raise Required("Email")
        if not password: raise Required("Password")
        SQL = Query("users").insert(
            name = name,
            email = email,
            password = password,
        ).SQL()
