# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(#q7ox+9%8udbb9n@9s@8#%k*i-=i#qnx#n8r4ed!5$137__m0'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}