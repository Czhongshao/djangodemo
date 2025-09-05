# djangodemo/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', include('games.urls')),  # 包含 games 应用的 URL 配置
]
