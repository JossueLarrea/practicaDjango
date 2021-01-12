from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="clientes"),
    path('crearClientes', views.crearCliente, name="crearClientes"),
    path('modificar_clientes/<int:cedula>/',
         views.modificarCliente, name="modificar_clientes"),
    path('eliminar_clientes/<int:cedula>/',
         views.eliminarCliente, name="eliminar_clientes"),


    path('cuentas/<int:cedula>/', views.listarCuentas, name="cuentas"),
    path('crearCuentas/<int:cedula>/', views.crearCuenta, name="crearCuentas"),
    path('modificar_cuentas/<int:numero>/',
         views.modificarCuenta, name="modificar_cuentas"),
    path('eliminar_cuentas/<int:numero>/',
         views.eliminarCuenta, name="eliminar_cuentas"),
]

