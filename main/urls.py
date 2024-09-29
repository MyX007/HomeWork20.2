from django.urls import path
from django.views.decorators.cache import cache_page

from main.views import ProductDetailView, ProductsListView, ContactView, ProductCreateView, ProductUpdateView, ProductDeleteView
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', cache_page(60)(ProductsListView.as_view()), name='index'),
    path('contact/', ContactView.as_view(), name='contact',),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]
