from django.contrib import messages
from django.db.models import QuerySet
from django.shortcuts import render, redirect

from .forms import *
from .models import *


def inicioDef(request):
    return render(request, 'inicio.html', {})

def loginSesionDef(request):
    if request.method == 'GET':
        return render(request, 'inicio.html', {})
    else:
        usuarioStr = request.POST.get('userIntx')
        passswordStr = request.POST.get('passwordInPs')
        try:
             print(usuarioStr,passswordStr)
             usuario = Usuario.objects.get(usuario=usuarioStr, password=passswordStr)
             print(usuarioStr, passswordStr)
             return render(request, "menu.html", { "usuarioStr":usuario.usuario})
        except Usuario.DoesNotExist:
            return render(request,"inicio.html",{"err":"Usuario o contraseña no son correctos"})

def registrarusuario(request):
    usuario = request.POST['txtusuario']
    password = request.POST['setpassword']

    usuario1 = Usuario.objects.create(
        usuario=usuario, password=password )
    messages.success(request, '¡Usuario registrado!')
    return redirect('inicioUrl')

def ClientesDef(request):
    Clientes: QuerySet[cliente] = cliente.objects.all()
    form_personal = Clienteform()
    context ={
        'Clientes':Clientes,
        'form_personal' : form_personal

    }
    return render(request, 'Clientes.html', context)


def add_ClientesDef(request):
    if request.POST:
        form = Clienteform(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"Error al guardar")
                return redirect('Clientes')
    return redirect('Clientes')

def add_ComprasDef(request):
    if request.POST:
        form = Comprasform(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"Error al guarder")
                return redirect('Compras')
    return redirect('Compras')
def ComprasDef(request):
    D_Compras: QuerySet[compras] = compras.objects.all()
    form_personal = Comprasform()
    context ={
        'D_Compras':D_Compras,
        'form_personal' : form_personal

    }
    return render(request, 'Compra.html', context)





def VentasDef(request):
    D_ventas = ventas.objects.all()
    form_personal = Ventasform()
    context ={
        'D_ventas':D_ventas,
        'form_personal' : form_personal

    }
    return render(request, 'Ventas.html', context)


def add_VentaDef(request):
    #print('GUARDAR CLIENTE')
    if request.POST:
        form = Ventasform(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"Error al guardar")
                return redirect('Ventas')
    return redirect('Ventas')


def eliminarVenta(request,id):
    venta = ventas.objects.get(id=id)
    venta.delete()

    messages.success(request, '¡VENTA eliminada!')
    return redirect('inicioUrl')