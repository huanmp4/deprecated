"""
Django settings for xfz02 project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's=rl3ghy&&txqbc5=6k+01&2nzl%6^9nzr(%)*7w7@oc89y_1u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['122.114.157.40','106.13.7.98','127.0.0.1','ambulance176.site','www.ambulance176.site']


# Application definition

INSTALLED_APPS = [
    'apps.legend',
    'apps.testapp',
    'apps.register',
    'apps.news',
    'apps.cms',
    'apps.course',
    'apps.payinfo',
    'apps.search',
    'apps.ueditor',
    'apps.party',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'xfz02.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'front','templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': ['django.templatetags.static'],

        },
    },
]

#确定'builtins': 'django.templatetags.static',是要加中括号吗？

WSGI_APPLICATION = 'xfz02.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xfz02',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

CACHES = {
    'default':{
        'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION':'127.0.0.1:11211',
        'KEY_FUNCTION':lambda key,prefix_key,version:'django:%s'%key
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

DEBUG_TOOLBAR_PANELS = [
    # 代表是哪个django版本
    'debug_toolbar.panels.versions.VersionsPanel',
    # 用来计时的，判断加载当前页面总共花的时间
    'debug_toolbar.panels.timer.TimerPanel',
    # 读取django中的配置信息
    'debug_toolbar.panels.settings.SettingsPanel',
    # 看到当前请求头和响应头信息
    'debug_toolbar.panels.headers.HeadersPanel',
    # 当前请求的想信息（视图函数，Cookie信息，Session信息等）
    'debug_toolbar.panels.request.RequestPanel',
    # 查看SQL语句
    'debug_toolbar.panels.sql.SQLPanel',
    # 静态文件
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    # 模板文件
    'debug_toolbar.panels.templates.TemplatesPanel',
    # 缓存
    'debug_toolbar.panels.cache.CachePanel',
    # 信号
    'debug_toolbar.panels.signals.SignalsPanel',
    # 日志
    'debug_toolbar.panels.logging.LoggingPanel',
    # 重定向
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DISABLE_PANELS = {'debug_toolbar.panels.profiling.ProfilingPanel','debug_toolbar.panels.versions.VersionsPanel','debug_toolbar.panels.settings.SettingsPanel'}

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
    # Toolbar options
    'RESULTS_CACHE_SIZE': 3,
    'SHOW_COLLAPSED': True,
    # Panel options
    'SQL_WARNING_THRESHOLD': 100,   # milliseconds
}



# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'front','district'),
    os.path.join(BASE_DIR,'front','source'),
    os.path.join(BASE_DIR,'front','templates'),
    os.path.join(BASE_DIR,'front','templates','legendtaotian')
]

STATIC_ROOT = os.path.join(BASE_DIR,'static_dist')

AUTH_USER_MODEL = 'register.User'

# CLIENTIMAGE_URL = '/front/source/client_image/'
# CLIENTIMAGE_ROOT = os.path.join(BASE_DIR,'front','source','client_image')
CLIENTIMAGE_URL = '/static/client_image/'
CLIENTIMAGE_ROOT = os.path.join(BASE_DIR,'static_dist','source','client_image')



#七牛
# Qiniu配置
QINIU_ACCESS_KEY = 'L7Idi7_0oH-8LC1g2CjLb1h9Z6kN4-JLoqoOn21U'
QINIU_SECRET_KEY = 'IGhDFYcbCns_3RcEopOwmHLE8M7XctIe_bVwYfHr'
QINIU_BUCKET_NAME = 'establish'
QINIU_DOMAIN = 'http://q1wvz08zi.bkt.clouddn.com/'

# 七牛和自己的服务器，最少要配置一个
# UEditor配置
UEDITOR_UPLOAD_TO_QINIU = True
UEDITOR_QINIU_ACCESS_KEY = QINIU_ACCESS_KEY
UEDITOR_QINIU_SECRET_KEY = QINIU_SECRET_KEY
UEDITOR_QINIU_BUCKET_NAME = QINIU_BUCKET_NAME
UEDITOR_QINIU_DOMAIN = QINIU_DOMAIN

#ueditor
UEDITOR_UPLOAD_TO_SERVER = True
UEDITOR_UPLOAD_PATH = CLIENTIMAGE_ROOT
UEDITOR_CONFIG_PATH = os.path.join(BASE_DIR,'front','district','ueditor','config.json')

#page加载新闻数量

PAGE_LOAD_NUM = 1



HAYSTACK_CONNECTIONS = {
    'default':{
        'ENGINE':'apps.news.whoosh_cn_backend.WhooshEngine',
        'PATH':os.path.join(BASE_DIR,'whoosh_index')
    }
}
#verify环境
#1.pip install haystack
#2.pip install whoosh
#3.settings 添加HAYSTACK_CONNECTIONS,并在目录添加'whoosh_index'文件夹,用来存储缓存
#4.在News 的app下创建search_indexes.py
#5.在Search 的app下创建indexes文件夹
#6.Search app的url更改为haystack include
#7.html模板把newses数据改为result.object
#8.python manage.py rebuild_index 把数据存储到缓存
#9.把path('index',include('haystack.urls'),name='haysta') 加入url并和search搜索框同名
#10.复制News app下的whoosh_cn_backend

#11.增删改后自动创建索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 3

