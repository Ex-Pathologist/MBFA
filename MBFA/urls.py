from django.contrib import admin
from django.urls import path
from MBFA.views import home, statistics, improvement, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('statistics', statistics),
    path('improvement', improvement),
    path('about/', about),
]
