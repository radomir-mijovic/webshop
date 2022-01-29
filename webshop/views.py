from rest_framework.generics import ListAPIView
from .serializers import ProductsSerializer
from .models import Products


class ProductsListView(ListAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
