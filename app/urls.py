from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),

    #vistas
    path('', include('src.routers.urls')),

    
    path("reactpy/", include("reactpy_django.http.urls")),
]
