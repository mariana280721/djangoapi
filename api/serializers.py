from rest_framework import serializers
from api.models import Producto

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
#        exclude = ['id']
#        fields = ['codigo', 'nombre' , 'descripcion' , 'precio']

        fields = '__all__'