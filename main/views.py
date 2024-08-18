from django.shortcuts import render
from main.models import Product
# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView


class ProductsListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Свяжитесь с нами'

