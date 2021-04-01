# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')5&x(5x(4v)pmxxxjc%@i^=ay09rsn3o%&v)sy8=g8*2554c&#'


DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shopnn',
        'USER': 'psqladmin',
        'PASSWORD': 'a_Pbase_r',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
