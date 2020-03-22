from django.urls import path
from . import views
app_name = "legendattach"
urlpatterns = [
    path('test',views.index,name="test"),
    path('visit',views.visit,name="visit"),
    path('check',views.check,name="check"),
]