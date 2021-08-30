from django.urls import path
from TauraikApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('tienda/', views.tienda, name="Tienda"),
]

#Agregar el directorio Media para ver la imagen desde el panel de admin
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)