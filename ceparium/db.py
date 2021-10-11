import os

""" BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 """
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'dbCeparium',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}