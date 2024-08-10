from django.urls import path
from main.views import home, contact, product
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', home, name='index'),
    path('contact/', contact, name='contact',),
    path('product/<int:pk>', product, name='product')
]
