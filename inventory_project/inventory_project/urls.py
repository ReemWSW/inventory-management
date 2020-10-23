
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
    path('auth/',include(('authentication.urls', 'authentication'), namespace='auth')),
]
