from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm
from django.http import HttpResponseRedirect


# Create your views here.

#Funcion para el index
def index(request):
    return render(request, 'index.html')


#Funcion para productos
def productos(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, 'productos.html', context)


#Funcion para carro
def agregar_al_carro(request, product_id):
    producto = get_object_or_404(Producto, product_id=product_id)
    carro = request.session.get('carro', {})

    if str(product_id) in carro:
        carro[str(product_id)]['cantidad'] += 1
    else:
        carro[str(product_id)] = {'producto': producto.product_name, 'cantidad': 1}

    request.session['carro'] = carro
    return redirect('productos')

def carro(request):
    carro = request.session.get('carro', {})
    items = []
    for key, value in carro.items():
        product = Producto.objects.get(product_id=key)
        items.append({'producto': product, 'cantidad': value['cantidad']})
    context = {
        'carro': items
    }
    return render(request, 'carro.html', context)

def ver_carro(request):
    productos_en_carro = []
    for item in carro.values():
        productos_en_carro.append(item)
    return render(request, 'carro.html', {'carro': productos_en_carro})

def eliminar_del_carro(request, product_id):
    carro = request.session.get('carro', {})

    if str(product_id) in carro:
        if carro[str(product_id)]['cantidad'] > 1:
            carro[str(product_id)]['cantidad'] -= 1
        else:
            del carro[str(product_id)]

        request.session['carro'] = carro

    return redirect('carro')

def eliminar_una_unidad(request, product_id):
    carro = request.session.get('carro', {})

    if str(product_id) in carro:
        if carro[str(product_id)]['cantidad'] > 1:
            carro[str(product_id)]['cantidad'] -= 1
        else:
            del carro[str(product_id)]

        request.session['carro'] = carro

    return redirect('carro')


#Funcion del registro
def registro(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=name).exists():
                messages.error(request, 'El nombre de usuario ya existe')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'El correo electrónico ya está registrado')
            else:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.save()
                login(request, user)
                return redirect('index')  # Redirige a la página de inicio después del registro
        else:
            messages.error(request, 'Las contraseñas no coinciden')
    
    return render(request, 'registro.html')

#Funcion de ayuda
def ayuda(requets):
    return render(requets, 'ayuda.html')

#Funcion de stock
def stock(requets):
    return render(requets, 'stock.html')

#Funciones para el crud
def stock_crud(requets):

    productos=Producto.objects.all()
    context={'productos':productos}
    print("enviando datos stock")
    return render(requets, "stock.html", context)

def stockAdd(request):
    print("estoy en controlador stockAdd")
    if request.method == "POST":
        print("controlador es un POST...")
        form = ProductoForm(request.POST)
        if form.is_valid():
            print("estoy en agregar, is_valid")
            form.save()
            form = ProductoForm()
            context = {'mensaje': "OK, datos grabados...", 'form': form}
        else:
            context = {'form': form}
    else:
        form = ProductoForm()
        context = {'form': form}
    return render(request, 'stockAdd.html', context)

def stock_del(request, pk):
    print("estoy en controlador stock_del")
    producto = get_object_or_404(Producto, product_id=pk)
    if producto:
        producto.delete()
        mensaje = "Bien, datos eliminados..."
    else:
        mensaje = "Error, id no existe"
    productos = Producto.objects.all()
    context = {'productos': productos, 'mensaje': mensaje}
    return render(request, 'stock.html', context)

def stock_edit(request, pk):
    print("estoy en controlador stock_edit")
    producto = get_object_or_404(Producto, product_id=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            mensaje = "Bien, datos actualizados..."
            return redirect('stock')
        else:
            mensaje = "Error, datos no válidos"
    else:
        form = ProductoForm(instance=producto)
        mensaje = ""
    context = {'producto': producto, 'form': form, 'mensaje': mensaje}
    return render(request, 'stock_edit.html', context)

    
