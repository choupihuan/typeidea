from .base import * #NOQA



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_DB',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'PORT':'3306',

    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True