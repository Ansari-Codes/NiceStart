import uuid, os

# RUN OPTIONS
FAVICON = "👌"
APP_NAME = "NiceScript"
# HOST = '127.0.0.1'
# PORT = int(os.environ.get("PORT", 8080))
SECRET = str(uuid.uuid4().hex)

# THEME
THEME_DEFAULT = dict(
    primary = '#5898d4',
    secondary = '#26a69a',
    accent = '#9c27b0',
    dark = '#1d1d1d',
    positive = '#21ba45',
    negative = '#c10015',
    info = '#31ccec',
    warning = '#f2c037',
    btn = "#237bcd"
)

DB_CREDS = dict(
    ENGINE = 'sqlite',
    NAME = "database.sqlite",
)

MIGRATIONS_FOLDER = "db.Migrations"