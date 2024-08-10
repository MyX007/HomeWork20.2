from django.shortcuts import render
from main.models import Product
# Create your views here.


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'main/index.html', context)


def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'category': product.category,
        'title': 'Страница товара',
        'img' : product.img
    }
    return render(request, 'main/product.html', context)




def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f'{name} ({phone}) {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'main/contact.html', context)
