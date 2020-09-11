from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('reservas/', include('reservas.urls')),
    path('admin/', admin.site.urls),
]
