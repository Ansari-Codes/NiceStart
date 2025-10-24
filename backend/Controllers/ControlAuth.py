from library.dbQuery import Query
from db.db import RUN_SQL
from library.validations import IsValidEmail, IsValidName, StrengthOfPswd
from backend.Models.ModelAuth import Auth
TABLE = "users"

async def _is_unique(value: str, column: str):
    return not bool(await RUN_SQL(Query(TABLE).select(column).where(**{column: value}).SQL()))

async def _validate(values: dict) -> dict:
    name = values.get("name")
    email = values.get("email")
    pswd = values.get("password")
    errors = {}
    if name:
        if not IsValidName(name):
            errors['name'] = 'Name is invalid'
        elif not _is_unique(name, 'name'):
            errors['name'] = 'Name is already taken!'
    if email:
        if not IsValidEmail(email):
            errors['email'] = 'Email is invalid'
        elif not _is_unique:
            errors['email'] = 'Email is already taken!'
    if not pswd:
        errors['password'] = 'Password is required'
    elif StrengthOfPswd(pswd or '') < 4:
        errors['password'] = 'Password is weak!'
    return errors

async def create(data: dict) -> tuple[bool, dict]:
    errors = _validate(data)
    if not errors:
        result = await Auth().create(data)
    return False, {}