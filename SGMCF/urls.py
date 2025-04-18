from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('admin/', permanent=True)),
    path('temperatura/', include('temperatura.urls')),
])
