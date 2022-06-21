
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('indexing.urls', namespace='Index')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('rest_framework.urls')),
]
