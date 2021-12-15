from django.contrib import admin
from django.urls import path
from MBFA.views import home, statistics, improvement, about, regist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('statistics', statistics),
    path('improvement', improvement),
    path('about/', about),
    path('regist/', regist),
]
