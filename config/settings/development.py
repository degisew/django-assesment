from .base import *
from .base import INSTALLED_APPS, MIDDLEWARE

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='django-insecure-k65ej_62__q==m9t&z)(f8!&4i#urv$s0vb311nu_kj(rca8=%'
)

INSTALLED_APPS += ['debug_toolbar']


# print('######################', INSTALLED_APPS)
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend",
)

INTERNAL_IPS = [
    "127.0.0.1",
]
