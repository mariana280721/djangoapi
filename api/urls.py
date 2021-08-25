from django.urls import path
from .views import Producto_APIView


urlpatterns = [
    path('api', Producto_APIView.as_view()),

]
