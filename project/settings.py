# FILE: /project/settings.py

"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from django.contrib.messages import constants #1:

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*qz=i5xtlf22k!sv+u=o=0k6zwwwlih6tofvl#lblyn-=iu4sa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar', #2:
    'product', #14:
    'order', #15:
    'client_profile', #15:
    'crispy_forms', #16:
    'crispy_bootstrap4', #16:
]

CRISPY_TEMPLATE_PACK = 'bootstrap4' #17:

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware', #3:
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], #4:
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us' # 'pt-BR'

TIME_ZONE = 'UTC' # 'America/Sao_paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') #5:
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates/static')] #6: #18:
MEDIA_URL = '/media/' #7:
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #8:

MESSAGE_TAGS = { #9:
    constants.DEBUG: 'alert-info',
    constants.ERROR: 'alert-danger',
    constants.INFO: 'alert-info',
    constants.SUCCESS: 'alert-success',
    constants.WARNING: 'alert-warning',
}

# Session in days: 60s * 60m * 24h * 1d
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 #10:

# Save earch request
SESSION_SAVE_EVERY_REQUEST = False #11:

# Serializer - JSON Standard
# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer' #12:

INTERNAL_IPS = [ #13:
    '127.0.0.1',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ------------------------------------------------------------------
#18: 'BASE_DIR' adicionado, esqueci de adicionar.
# ------------------------------------------------------------------
#16: Adiciona crispy_forms e crispy_bootstrap4 às aplicações instaladas para suportar a formatação de formulários com o framework Bootstrap 4.
#17: Define o pacote de templates do crispy_forms para usar o Bootstrap 4.
# ------------------------------------------------------------------
#15: Estes são nomes dos aplicativos, que foi adicionado à lista INSTALLED_APPS. Isso significa que o Django reconhecerá e ativará estes apps, permitindo que suas funcionalidades (modelos, views, etc.) sejam integradas ao projeto.
# ------------------------------------------------------------------
#14: Adiciona o aplicativo product à lista INSTALLED_APPS no arquivo settings.py, o que indica que este aplicativo deve ser carregado e utilizado pelo projeto Django.
# ------------------------------------------------------------------
#1: Esta linha importa o módulo constants do pacote django.contrib.messages. Ele contém as constantes usadas para definir as tags de nível de mensagem, como DEBUG, ERROR, INFO, SUCCESS, etc. Essas constantes são utilizadas para associar mensagens a classes CSS no frontend. Este módulo é parte da biblioteca de mensagens do Django.
#2: Adiciona o pacote debug_toolbar às aplicações instaladas do Django. O Django Debug Toolbar é uma ferramenta usada em desenvolvimento para inspecionar e debugar a execução de código no Django, mostrando informações como consultas SQL executadas, tempos de resposta, entre outros detalhes. Essa linha comunica que o Django está usando esse pacote como parte de suas INSTALLED_APPS.
#3: Adiciona o middleware do debug_toolbar, que intercepta as requisições e permite que o Debug Toolbar funcione, exibindo uma barra de ferramentas de depuração no navegador durante o desenvolvimento.
#4: Define o caminho dos diretórios de templates. Aqui, a pasta 'templates' é unida ao diretório base do projeto, indicando onde o Django deve buscar arquivos de template (HTML, por exemplo). Isso comunica que o Django deve procurar templates personalizados na pasta templates.
#5: Define o diretório para onde os arquivos estáticos serão coletados quando o comando collectstatic for executado. Esses arquivos incluem CSS, JavaScript e imagens.
#6: Especifica diretórios adicionais onde os arquivos estáticos podem ser encontrados. Aqui, aponta para uma pasta chamada templates/static, que pode conter arquivos CSS ou JS associados aos templates.
#7: Define a URL base para acessar os arquivos de mídia (arquivos carregados pelo usuário, como imagens e vídeos). A URL será /media/.
#8: Define o diretório onde os arquivos de mídia serão armazenados fisicamente. O diretório será BASE_DIR/media.
#9: Mapeia os níveis de mensagem definidos pelo módulo constants para classes CSS. As mensagens como DEBUG, ERROR, INFO, etc., serão convertidas para as classes de alerta correspondentes, como 'alert-info', 'alert-danger', etc. Isso facilita a estilização das mensagens no frontend.
#10: Define o tempo de expiração do cookie de sessão, em segundos. Aqui, o tempo é definido para 7 dias (60 segundos * 60 minutos * 24 horas * 7 dias).
#11: Indica que as sessões não serão salvas a cada requisição. Se fosse True, o Django salvaria a sessão em cada requisição, mesmo que ela não tenha sido modificada, o que poderia gerar overhead desnecessário.
#12: Esta linha comentada especifica o tipo de serializador que seria usado para armazenar as sessões. O PickleSerializer serializa os dados da sessão usando o Python pickle. Se fosse ativada, essa configuração indicaria que as sessões seriam armazenadas de forma serializada (pickle), mas foi desativada por segurança e desempenho.
#13: Define uma lista de IPs que são considerados internos, o que normalmente se refere ao ambiente de desenvolvimento local. O IP 127.0.0.1 é o endereço de loopback (localhost).

# https://linktr.ee/edsoncopque