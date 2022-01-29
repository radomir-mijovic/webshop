from rest_framework.generics import ListCreateAPIView
from .serializers import ProductsSerializer
from .models import Products


class ProductsListView(ListCreateAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
