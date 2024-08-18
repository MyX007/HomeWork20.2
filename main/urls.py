from django.urls import path
from main.views import ProductDetailView, ProductsListView, ContactView
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact',),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product')
]
