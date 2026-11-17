from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #Definimos acceso al panel admin
    path('', include('canchas.urls')), # recibe peticiones de la web y la redirige a la app
]
