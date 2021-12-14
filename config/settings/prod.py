from .base import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', "sheltered-atoll-07813"]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASE_URL = os.environ.get('DATABASE_URL')
db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)
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

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')