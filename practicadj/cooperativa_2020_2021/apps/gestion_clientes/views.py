from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.modelo.models import Cliente, Cuenta
from .forms import FormularioCliente, FormularioCuenta, ClienteUpdate, CuentaUpdate


def index(request):
    listaClientes = Cliente.objects.all()
    return render(request, 'clientes/index.html', locals())


def crearCliente(request):
    formulario_cliente = FormularioCliente(request.POST)
    formulario_cuenta = FormularioCuenta(request.POST)
    if request.method == 'POST':
        if formulario_cliente.is_valid() and formulario_cuenta.is_valid():
            cliente = Cliente()
            datos_cliente = formulario_cliente.cleaned_data
            cliente.cedula = datos_cliente.get('cedula')
            cliente.nombres = datos_cliente.get('nombres')
            cliente.apellidos = datos_cliente.get('apellidos')
            cliente.genero = datos_cliente.get('genero')
            cliente.estadoCivil = datos_cliente.get('estadoCivil')
            cliente.correo = datos_cliente.get('correo')
            cliente.telefono = datos_cliente.get('telefono')
            cliente.celular = datos_cliente.get('celular')
            cliente.direccion = datos_cliente.get('direccion')
            # ORM
            cliente.save()

            cuenta = Cuenta()
            datos_cuenta = formulario_cuenta.cleaned_data
            cuenta.numero = datos_cuenta.get("numero")
            cuenta.saldo = datos_cuenta.get("saldo")
            cuenta.tipoCuenta = datos_cuenta.get("tipoCuenta")
            cuenta.cliente = cliente
            # ORM
            cuenta.save()
        return redirect(index)
    return render(request, 'clientes/crearClientes.html', locals())


def modificarCliente(request, cedula):
    cliente = Cliente.objects.get(cedula=cedula)
    if request.method == 'GET':
        formulario_cliente_editar = ClienteUpdate(instance=cliente)
    else:
        formulario_cliente_editar = ClienteUpdate(
            request.POST, instance=cliente)
        if formulario_cliente_editar.is_valid():
            formulario_cliente_editar.save()
        return redirect(index)
    return render(request, 'clientes/modificar.html', locals())


def eliminarCliente(request, cedula):
    cliente = Cliente.objects.get(cedula=cedula)
    if request.method == 'POST':
        cliente.delete()
        return redirect(index)
    return render(request, 'clientes/eliminar.html', locals())


def listarCuentas(request, cedula):
    cliente = Cliente.objects.get(cedula=cedula)
    cuentas = Cuenta.objects.filter(cliente=cliente)
    return render(request, 'cuentas/index.html', locals())


def crearCuenta(request, cedula):
    formulario_cuenta = FormularioCuenta(request.POST)
    cliente = Cliente.objects.get(cedula=cedula)
    if request.method == 'POST':
        if formulario_cuenta.is_valid():
            cuenta = Cuenta()
            datos_cuenta = formulario_cuenta.cleaned_data
            cuenta.numero = datos_cuenta.get("numero")
            cuenta.saldo = datos_cuenta.get("saldo")
            cuenta.tipoCuenta = datos_cuenta.get("tipoCuenta")
            cuenta.cliente = cliente
            # ORM
            cuenta.save()
        return redirect(index)
    return render(request, 'cuentas/crear.html', locals())


def modificarCuenta(request, numero):
    cuenta = Cuenta.objects.get(numero=numero)
    if request.method == 'GET':
        formulario_cuenta_editar = CuentaUpdate(instance=cuenta)
    else:
        formulario_cuenta_editar = CuentaUpdate(
            request.POST, instance=cuenta)
        if formulario_cuenta_editar.is_valid():
            formulario_cuenta_editar.save()
        return redirect(index)
    return render(request, 'cuentas/modificar.html', locals())


def eliminarCuenta(request, numero):
    cuenta = Cuenta.objects.get(numero=numero)
    if request.method == 'POST':
        cuenta.delete()
        return redirect(index)
    return render(request, 'cuentas/eliminar.html', locals())