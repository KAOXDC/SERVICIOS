from django.urls import path, include
from rest_framework import routers
from home.models import *
from webservices.views import *

router = routers.DefaultRouter()
router.register(r'productos', producto_viewset)
router.register(r'marcas', marca_viewset)
router.register(r'categorias', categoria_viewset)

urlpatterns = [
		path('api/', include(router.urls)),
		path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]
