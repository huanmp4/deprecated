from django.urls import path
from .import views

app_name = 'flew'
urlpatterns = [
    path('',views.index,name='index'),
]