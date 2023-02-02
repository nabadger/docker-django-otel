from django.urls import re_path
from django.contrib import admin
from app.views import app

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', app)
]
