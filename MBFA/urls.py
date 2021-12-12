from django.contrib import admin
from django.urls import path
from MBFA.views import home, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('about/', about)
]
