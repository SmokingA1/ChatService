from decouple import config

DATABASE_URL = config("DATABASE_URL")
SECRET_KEY = config("SECRET_KEY", default='default_secret_key')
DEBUG = config("DEBUG", cast=bool) # cast converts value to bool, int, list, etc.
