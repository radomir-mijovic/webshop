from django.urls import path
from .views import *

app_name = 'webshop'

urlpatterns = [
    path('homepage', ProductsListView.as_view(), name='homepage'),
]