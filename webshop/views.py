from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .serializers import ProductsSerializer
from .models import Products
from rest_framework import filters


class ProductsListView(ListCreateAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    filter_backends = [
        filters.SearchFilter
    ]
    search_fields = [
        'name', 'code', 'brand'
    ]

    def post(self, request, *args, **kwargs):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response(serializer.errors, 400)


class ProductDetailView(RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        product = Products.objects.get(slug=kwargs['slug'])
        serializer = ProductsSerializer(product)
        return Response(serializer.data)
