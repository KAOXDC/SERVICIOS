from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
from django.http import JsonResponse

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, DeleteView, UpdateView)

from django.http import HttpResponse
from django.core import serializers

import requests
from django.contrib.auth.models import Permission
import json


# LOS METODOS PARA EL CONSUMO DE SERVICIOS WEB ESTAN EN LAS SIGUIENTES FUNCIONES
#	metodo_get()
#	metodo_post()
#	metodo_put()
#	metodo_delete()

def ws_productos_vista(request):
	data = serializers.serialize('json',Producto.objects.filter(status = True))
	return HttpResponse(data, content_type='application/json')

	'''
	data = list(Producto.objects.values())
	return JsonResponse(data, safe=False)
	'''


def vista_about(request):
	respuesta = metodo_get()
	return render(request,'about.html',locals())

def vista_agregar_producto(request):

	get_marcas = requests.get('http://localhost:8000/api/marcas/')
	get_catego = requests.get('http://localhost:8000/api/categorias/')

	marcas = get_marcas.json()
	ctegrs = get_catego.json()

	lis_marcas=[]
	lis_ctegrs=[]

	for m in marcas:
		p= m['id'], m['nombre'], m['url']
		lis_marcas.append(p)

	for c in ctegrs:
		p= c['id'], c['nombre'], c['url']
		lis_ctegrs.append(p)

	if request.method == 'POST':			

		nombre = request.POST.get('nombre')
		descripcion = request.POST.get('descripcion')
		status = request.POST.get('status')
		precio = request.POST.get('precio')
		stock = request.POST.get('stock')
		categorias = request.POST.getlist('categoria')
		marca = request.POST.get('marca')



		#print(nombre,'**',descripcion,'**',status,'**',precio,'**',stock,'**',categorias,'**',marca)
		metodo_post(nombre,descripcion,status,precio,stock,categorias,marca)


		'''prod = formulario.save(commit = False)
		prod.status = True
		prod.save()
		formulario.save_m2m()'''

		return  redirect ('/lista_producto/')

	return render(request, 'vista_agregar_producto.html', locals())

	#variable=request.POST.get('marca')

def vista_editar_producto(request, id_prod):
	prod = Producto.objects.get(id=id_prod)
	if request.method == "POST":
		formulario = agregar_producto_form(request.POST, request.FILES, instance=prod)
		if formulario.is_valid():
			
			nombre = formulario.cleaned_data['nombre']
			descripcion = formulario.cleaned_data['descripcion']
			status = formulario.cleaned_data['status']
			precio = formulario.cleaned_data['precio']
			stock = formulario.cleaned_data['stock']
			categorias = formulario.cleaned_data['categorias']
			marca = formulario.cleaned_data['marca']

			m = Marca.objects.get(nombre=marca)

			c = []
			for i in categorias:
				cat = Categoria.objects.get(nombre=i)
				c.append("http://localhost:8000/api/categorias/"+str(cat.id)+"/")

			
			metodo_put(prod.id,nombre,descripcion,status,precio,stock,c,m.id)

			return  redirect ('/lista_producto/')
	else:
		formulario = agregar_producto_form(instance = prod)
	return render(request, 'vista_agregar_producto.html', locals())


def vista_eliminar_producto(request, url):
	metodo_delete(url)
	return  redirect ('about')


def vista_contacto(request):
	info_enviado = False
	email = ""
	title = ""
	text = ""
	if request.method == "POST":
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['correo']
			title = formulario.cleaned_data['titulo']
			text  = formulario.cleaned_data['texto']
	else:
		formulario = contacto_form()
	return render(request,'contacto.html',locals())

def vista_lista_producto (request):
	lista = Producto.objects.filter()
	return render(request, 'lista_producto.html', locals())


def vista_ver_producto(request, id_prod):
	p = Producto.objects.get(id=id_prod)
	return render(request,'ver_producto.html',locals())


def vista_login (request):
	usu = ""
	cla = ""
	if request.method == "POST":
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu, password=cla)
			if  usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/lista_producto/')
			else:
				msj = "usuario o clave incorrectos"
	formulario = login_form()
	return render(request, 'login.html', locals())

def vista_logout (request):
	logout(request)
	return redirect('accounts/login/')


def vista_register (request):
	formulario = register_form()
	if request.method == 'POST':
		formulario = register_form(request.POST)
		if formulario.is_valid():
			usuario = formulario.cleaned_data['username']
			correo = formulario.cleaned_data['email']
			password_1 = formulario.cleaned_data['password_1']
			password_2 = formulario.cleaned_data['password_2']
			u = User.objects.create_user(username=usuario, email=correo, password=password_1)
			u.save()
			return render(request, 'tanks_for_register.html', locals())
		else:
			return render(request, 'register.html', locals())	
	return render(request, 'register.html', locals())





#================================================================#
#======================                       ===================#
#======================  CONSUMO DE SERVICIOS  ==================#
#======================                       ===================#
#================================================================#


def metodo_get():

	peticion = requests.get('http://localhost:8000/api/productos/')

	respuesta = peticion.json()
	lista = []
	for i in respuesta:
		cadena = i['url']
		l   = len(cadena)
		id_ = cadena[l-2]
		p   = i['nombre'], id_
		lista.append(p)

	#respons = str(respuesta).strip('[]')

	'''
	id = {"id":"1"}

	peticion = requests.get('http://localhost:8000/api/productos/', params = id)
	peticion.status_code

	respuesta = peticion.json()'''

	return lista

def metodo_post(nombre,descripcion,status,precio,stock,categorias,marca):

	dato = {

        "nombre": nombre,
        "descripcion": descripcion,
        "status": status,
        "precio": precio,
        "stock": stock,
        "marca": marca,
        "categorias": categorias
    }

	peticion = requests.post('http://localhost:8000/api/productos/', data = dato)
	peticion.status_code

	respuesta = peticion.json()

	'''
	datos = {"nombre":"Ejercicio POST"}

	peticion = requests.post('http://localhost:8000/api/marcas/', data = datos)
	peticion.status_code

	respuesta = peticion.json()
	'''
	return respuesta


def metodo_delete(id):
	url = 'http://localhost:8000/api/productos/'
	peticion = requests.delete(url+id+'/') #, params=id)
	peticion.status_code

	print('Se supone que esta eliminado',url)

def metodo_put(id,nombre,descripcion,status,precio,stock,categorias,marca):

	dato = {

        "nombre": nombre,
        "descripcion": descripcion,
        "status": status,
        "precio": precio,
        "stock": stock,
        "marca": "http://localhost:8000/api/marcas/"+str(marca)+"/",
        "categorias": categorias
    }


	url = 'http://localhost:8000/api/productos/'+str(id)+'/'

	peticion = requests.put(url, data=dato) #, params=id)
	peticion.status_code

	return peticion


def persona(request):

	u = User.objects.create_user(username='Prueba4', password= '123qwe')
	u.is_staff=True
	u.user_permissions.add(cliente)
	u.save()

	#return redirect('about')
	return render(request,'about.html',locals())


#=======================================================#
#================                  =====================#
#================ Class_Based_Views ====================#
#=================                 =====================#
#=======================================================#
class class_agregar_producto(CreateView):
	model = Producto
	fields= ['nombre','descripcion','status','precio','stock','categorias','marca','foto']
	success_url = reverse_lazy('productos')
#=======================================================#
class list_view(ListView):
	model = Producto
#=======================================================#
class class_detail_producto(DetailView):
	model = Producto
#=======================================================#
class class_edit_producto(UpdateView):
	model = Producto
	fields= ['nombre','descripcion','status','precio','stock','categorias','marca','foto']
	template_name_suffix = '_form'
	success_url = reverse_lazy('productos')
	#def get_success_url(self):
	#	return reverse_lazy('productos', args=[self.objects.id])
#=======================================================#