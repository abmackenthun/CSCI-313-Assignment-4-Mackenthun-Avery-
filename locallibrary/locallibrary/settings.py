 import os
 
 INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add our new application
    'catalog.apps.CatalogConfig', # This object was created for us in /catalog/apps.py
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

TIME_ZONE = 'Centeral'

MIDDLEWARE=[
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

 TEMPLATES = [
      {
       'DIRS': [os.path.join(BASE_DIR, 'templates')],
       'APP_DIRS': True,
      }
 ]

 LOGIN_REDIRECT_URL = '/'