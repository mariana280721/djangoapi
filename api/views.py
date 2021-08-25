from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import ProductoSerializers
from .models import Producto
from rest_framework import status
from rest_framework.decorators import action

class Producto_APIView(ModelViewSet):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializers


"""
class Post_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializers(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""