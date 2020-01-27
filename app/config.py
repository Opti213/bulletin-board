from starlette.config import Config
from starlette.datastructures import URL

config = Config(".env")

DB_CONNECTION = config("DB_CONNECTION", cast=URL)
