from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSeriallizer

#class base
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeriallizer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeriallizer

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeriallizer
    lookup_field ='pk'

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeriallizer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)



# mixins 
# class ProductMixin(
#     mixins.RetrieveModelMixin,
#     mixins.ListModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView
#     ):
    
#     queryset = Product.objects.all()
#     serializer_class = ProductSeriallizer
#     lookup_field = 'pk'

#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)




# CRUD function 
# @api_view(['GET', 'POST'])
# def profuct_view(request,pk=None, *args, **kwargs):
#     method = request.method
#     if method == 'GET':
#         if pk is not None:
#             #detail views
#             obj = get_object_or_404(Product , pk =pk)
#             data = ProductSeriallizer(obj, many=False).data
#             return Response(data)

#         # list
#         queryset = Product.objects.all()
#         data = ProductSeriallizer(queryset, many=True).data
#         return Response(data)

#     if method == 'POST':
#         #create item
#         serializer = ProductSeriallizer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response({'invalid request':'bad data'},status=400)

