from .base import *

SECRET_KEY = "secret_key"

# ------------- DATABASES -------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", "santa_claus"),
        "USER": env("POSTGRES_USER", "santa_claus"),
        "PASSWORD": env("POSTGRES_PASSWORD", "santa_claus"),
        "HOST": env("POSTGRES_HOST", "localhost"),
    }
}
