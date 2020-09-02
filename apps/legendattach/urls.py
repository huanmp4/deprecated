from django.urls import path
from . import views
from . import views_site
app_name = "legendattach"
urlpatterns = [
    path('test',views.index,name="test"),
    path('visit',views.visit,name="visit"),
    path('check',views.check,name="check"),
    path('cleanalldata', views.CleanAllData, name="cleanalldata"),
]


#传奇发布网
urlpatterns += [
    path("getdata",views_site.getData,name="getdata"),
    path("cleanDate",views_site.cleanDate,name="cleanDate")

]