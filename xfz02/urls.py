"""xfz02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from apps.news import views
from apps.legend import views as views_legend
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/',include('apps.news.urls')),
    path('',views.index,name='index'),
    path('cms/',include('apps.cms.urls')),
    path('register/',include('apps.register.urls')),
    path('course/',include('apps.course.urls')),
    path('pay/',include('apps.payinfo.urls')),
    path('search/',include('apps.search.urls')),
    path('ueditor/',include('apps.ueditor.urls')),
    path('party/',include('apps.party.urls')),
    path('legend',views_legend.index),
    path('legend',include('apps.legend.urls')),
    path('legendattach/',include('apps.legendattach.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns