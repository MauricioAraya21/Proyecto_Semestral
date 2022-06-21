from django.urls import path
from .views import agregar_producto, eliminar_producto, index,formulario, limpiar_carrito, restar_producto, tienda

urlpatterns = [
    path('', index, name="index_central"),
    path('formulario/', formulario, name="Formulario"),
    path('tienda/', tienda, name="Tienda"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]

