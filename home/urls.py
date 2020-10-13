from django.urls import path 
from django.views.generic import TemplateView
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	
	#     En esta vista estoy llamando los metodos de ws #

	path('',vista_about, name='about'),


	path('contacto/',vista_contacto, name='vista_contacto'),
	path('lista_producto/',vista_lista_producto, name='vista_lista_producto'),
	path('agregar_producto/',vista_agregar_producto, name='vista_agregar_producto'),
	path('ver_producto/<int:id_prod>/', vista_ver_producto, name='vista_ver_producto'),
	path('editar_producto/<int:id_prod>/', vista_editar_producto, name='vista_editar_producto'),
	path('eliminar_producto/<str:url>/', vista_eliminar_producto, name='vista_eliminar_producto'),
	#path('accounts/login/',vista_login, name='vista_login'),
	#path('logout/',vista_logout, name='vista_logout'),
	path('register/',vista_register, name='vista_register'),
	path('ws/productos/',ws_productos_vista,name = 'ws_productos_vista'),

	#ListView
	path('productos/',list_view.as_view(), name= 'productos'),
	#CreatelView
	path('class_agregar_producto/',class_agregar_producto.as_view()),
	#DetailView
	path('producto/<int:pk>/',class_detail_producto.as_view()),
	#EditView
	path('edit/<int:pk>/',class_edit_producto.as_view()),
]
