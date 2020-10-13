from home.models import *
from .serializer import *					
from rest_framework import viewsets

class producto_viewset(viewsets.ModelViewSet):
	queryset = Producto.objects.all()
	serializer_class = producto_serializer

class marca_viewset(viewsets.ModelViewSet):
	queryset = Marca.objects.all()
	serializer_class = marca_serializer

class categoria_viewset(viewsets.ModelViewSet):
	queryset = Categoria.objects.all()
	serializer_class = categoria_serializer

# class ProductViewSet(viewsets.ModelViewSet):
# 	queryset = Producto.objects.all()
# 	serializer_class = ProductSerializer
	
# 	@detail_route(methods=['post'])
# 	def upload_docs(request):
# 		try:
# 			file = request.data['file']
# 		except KeyError:
# 			raise ParseError('Request has no resource file attached')
# 		product = Producto.objects.create(foto=file)