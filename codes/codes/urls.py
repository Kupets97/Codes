from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from search_code.views import CodeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('code/<str:code>', CodeView.as_view(), name='code'),
]
