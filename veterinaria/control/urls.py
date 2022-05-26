from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from control import views

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('vacunas',views.vacunas, name="Vacunas"),
    path('registro/', views.registro, name="Registro"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)