from rest_framework import serializers
from home.models import *

class producto_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Producto
		fields = ('url' ,'nombre','descripcion', 'status', 'foto', 'precio', 'stock', 'marca', 'categorias',)

class marca_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Marca
		fields = ('url', 'id','nombre', )

class categoria_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Categoria
		fields = ('url','id','nombre', )   

# class ProductSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Producto
# 		fields = (
# 			'image',
# 		)
