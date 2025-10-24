from .Model import Model, Required
from lib.dbQuery import Query
from datetime import datetime
from db.db import RUN_SQL

class Auth(Model):
    def __init__(self):
        super().__init__()
    
    async def _create(self, obj: dict):
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
        await RUN_SQL(SQL)
        FETCH = Query("users").select().where(
            name = obj.get(name)
        ).SQL()
        return await RUN_SQL(FETCH, True)

    async def create(self, obj: dict | list) -> dict | list:
        result = []
        if isinstance(obj, (tuple, list)):
            for o in obj:
                result_o = await self._create(o)
                result.append(result_o)
        elif isinstance(obj, dict):
            result = await self._create(obj)
        else:
            raise TypeError(f"Object can only be a dict, list or a tuple. Not a '{type(obj).__name__}'")
        return result