from django import forms
from django.views.generic.edit import UpdateView
from apps.modelo.models import Cliente, Cuenta


class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["cedula", "apellidos", "nombres",
                  "genero", "estadoCivil", "correo", "telefono", "celular", "direccion"]


class ClienteUpdate(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["apellidos", "nombres", "genero",
                  "estadoCivil", "correo", "telefono", "celular", "direccion"]


class FormularioCuenta(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ["numero", "tipoCuenta", "saldo"]

class CuentaUpdate(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ["tipoCuenta", "saldo"]