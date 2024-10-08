
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clientApp.urls')),
    path('doctors/', include('DoctorApp.urls')),
]