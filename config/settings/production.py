from .base import *




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='django-insecure-k65ej_62__q==m9t&z)(f8!&4i#urv$s0vb311nu_kj(rca8=%'
)


ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["example.com"])