from django.urls import path
from .views import *

app_name = 'webshop'

urlpatterns = [
    path('products', ProductsListView.as_view(), name='products'),
]