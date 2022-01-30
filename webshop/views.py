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
        'name', 'code'
    ]

    def post(self, request, *args, **kwargs):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 200)
        return Response(serializer.errors)


class ProductDetailView(RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        product = Products.objects.get(id=kwargs['pk'])
        serializer = ProductsSerializer(product)
        return Response(serializer.data)
