from django.contrib import admin
from django.urls import path, include
import os

# APP_VERSION = os.getenv('APP_VERSION', 'v1'),

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'api/', include('api.urls')),
]
