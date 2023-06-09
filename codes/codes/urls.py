from django.contrib import admin
from django.urls import path

from search_code.views import CodeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('code/<str:code>/', CodeView.as_view(), name='code'),
    path('code/<path:code>/', CodeView.as_view(), name='code'),
]
