from django.urls import path
from . import views

urlpatterns = [
    #Vista del inicio(index.html)
    path('', views.index, name='index'),

    #Vista del registro(registro.html)
    path('registro', views.registro, name='registro'),

    #Vista de productos(productos.html)
    path('productos', views.productos, name='productos'),

    #Vista del carro(carro.html)
    path('carro', views.carro, name='carro'),
    path('agregar_al_carro/<int:product_id>/', views.agregar_al_carro, name='agregar_al_carro'),
    path('carro/eliminar/<int:product_id>/', views.eliminar_del_carro, name='eliminar_del_carro'),
    path('carro/eliminar_una_unidad/<int:product_id>/', views.eliminar_una_unidad, name='eliminar_una_unidad'),

    #Vista de ayuda(ayuda.html)
    path('ayuda', views.ayuda, name='ayuda'),

    #Vista del crud(stock.html)
    path('stock_crud', views.stock_crud, name='stock_crud'),
    path('stockAdd', views.stockAdd, name='stockAdd'),
    path('stock_del/<str:pk>', views.stock_del, name='stock_del'),
    path('stock_edit/<str:pk>', views.stock_edit, name='stock_edit'),
    path('stock', views.stock, name='stock'),

]   
