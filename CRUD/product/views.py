from django.shortcuts import render
from rest_framework import generics, mixins

from .models import Product
from .serializers import ProductSeriallizer

class ProductMixin(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
    ):
    
    queryset = Product.objects.all()
    serializer_class = ProductSeriallizer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.update(request, *args, **kwargs)
        return self.create(request, *args, **kwargs)