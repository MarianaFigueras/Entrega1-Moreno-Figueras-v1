
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index),
    path('hola/',views.hola),
    path('about', views.about),
    path('mi-template/', views.mi_template),
    path('mi-template/<str:nombre>', views.tu_template),
    path('ver-pedidos', views.ver_pedidos, name='ver_pedidos'),
    # path('crear-pedido/<str:nombre>/<str:guarnicion>', views.crear_pedido),
    path('crear-pedido', views.crear_pedido, name='crear_pedido'),

]