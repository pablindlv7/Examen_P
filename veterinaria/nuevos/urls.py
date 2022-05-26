from django.urls import path

from nuevos import views

urlpatterns = [

    path('', views.nuevos, name="Nuevos"),
    
]