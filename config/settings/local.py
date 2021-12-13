from .base import *


DEBUG = True
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": 'db',
        "PORT": 5432,
    }
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = "ryanthornston@gmail.com"
# EMAIL_HOST_PASSWORD = "pseudoalias"

EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
ANYMAIL = {
    "MAILJET_API_KEY": os.getenv("MAILJET_API_KEY"),
    "MAILJET_SECRET_KEY": os.getenv("MAILJET_SECRET_KEY")
}

MAILJET_DAILY_LIMIT=os.getenv("MAILJET_DAILY_API_LIMIT")
