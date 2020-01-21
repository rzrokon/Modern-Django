from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='r#3b2^_ahw-^24ro48(0u=-oobzu#jqk3q0=vzjm20tyuq)++t')

DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = []