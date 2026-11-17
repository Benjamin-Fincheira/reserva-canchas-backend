import os
from pathlib import Path
#ruta de carpeta raiz 
BASE_DIR = Path(__file__).resolve().parent.parent #de settings a backend

SECRET_KEY = 'django-insecure-evaluacion-dos-secreta'#sello o firma digital interna
DEBUG = True
ALLOWED_HOSTS = [] #desde localhost o 127.0.0.1.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Obligatorio para la API django rest framework
    'canchas',         # aplicación
]

MIDDLEWARE = [ #filtros de seguridad que procesan cada peticion
    'django.middleware.security.SecurityMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware', 
    'django.middleware.common.CommonMiddleware', 
    'django.middleware.csrf.CsrfViewMiddleware', 
    'django.contrib.auth.middleware.AuthenticationMiddleware', 
    'django.contrib.messages.middleware.MessageMiddleware', 
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
    ] 
ROOT_URLCONF = 'backend.urls' #ruta de urls principal
#ahi se gestionan las llamadas a la api
TEMPLATES = [ #configuracion para la visualizacion del sistema
    {
         'BACKEND': 'django.template.backends.django.DjangoTemplates', 
         'DIRS': [], 
         'APP_DIRS': True, 
         'OPTIONS': { 
            'context_processors': [ 
                'django.template.context_processors.debug', 
                'django.template.context_processors.request', 
                'django.contrib.auth.context_processors.auth', 
                'django.contrib.messages.context_processors.messages', 
                ], 
            }, 
        }, 
    ] 
WSGI_APPLICATION = 'backend.wsgi.application'#punto de entrada wsgi conecta las peticiones web con django
DATABASES = { #define sqlite3 como base de datos
    'default': { 
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': BASE_DIR / 'db.sqlite3', #nombre de base de datos en sqlite3
        } 
    }
STATIC_URL = 'static/'#http://localhost:8000/static/