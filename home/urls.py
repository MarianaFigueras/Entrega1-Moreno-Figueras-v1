
from django.urls import path
from home import views

urlpatterns = [
    path('hola/',views.hola),
    path('mi-template/', views.mi_template),
    path('mi-template/<str:nombre>', views.tu_template),
    path('ver-pedidos', views.ver_pedidos),
    path('crear-pedido/<str:nombre>/<str:guarnicion>', views.crear_pedido),

]