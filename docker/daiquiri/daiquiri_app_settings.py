'''
Secret key, use something random in production
'''
SECRET_KEY = 'this is not a very secret key'

'''
Debug mode, don't use this in production
'''
DEBUG = True

'''
Use Celery to run tasks asyncronous
'''
ASYNC = False

'''
The list of URLs und which this application available
'''
ALLOWED_HOSTS = ['localhost', 'ip6-localhost', '127.0.0.1', '[::1]']

'''
The database connection to be used, see also:
http://rdmo.readthedocs.io/en/latest/configuration/databases.html
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'daiquiri_app',
        'USER': 'daiquiri',
        'PASSWORD': 'password',
        'HOST': 'daiquiri_mariadb',
        'PORT': '3306',
        'CLIENT': '172.%.%.%'
    },
    'tap': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'TAP_SCHEMA',
        'USER': 'daiquiri_tap',
        'PASSWORD': 'password',
        'HOST': 'daiquiri_mariadb',
        'PORT': '3306',
        'CLIENT': '172.%.%.%'
    },
    'data': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'daiquiri_data',
        'PASSWORD': 'password',
        'HOST': 'daiquiri_mariadb',
        'PORT': '3306',
        'CLIENT': '172.%.%.%'
    }
}

'''
Base URL Path to this application, i.e. /path for http://exaple.com/path/
'''
# BASE_URL = ''

'''
Use a custom registration workflow
'''
# AUTH_WORKFLOW = 'confirmation'
# AUTH_WORKFLOW = 'activation'

'''
E-Mail configuration
'''
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = '25'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = True

'''
E-Mail configuration
'''
# SENDFILE_BACKEND = 'sendfile.backends.development'
# SENDFILE_BACKEND = 'sendfile.backends.xsendfile'
