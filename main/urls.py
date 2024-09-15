from django.urls import path
from main.views import ProductDetailView, ProductsListView, ContactView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact',),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]
