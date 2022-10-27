from django.urls import path
from menu import views

urlpatterns = [
    path('menu/', views.ver_platos, name='ver_platos'),
    path('menu/crear/', views.crear_plato, name='crear_plato')
]
