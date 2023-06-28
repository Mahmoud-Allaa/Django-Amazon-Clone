from django.shortcuts import render
from django.views import generic
from .models import ProductImages, Product, Brand, Review


class ProductList(generic.ListView):
    model = Product

class ProductDetail(generic.DetailView):
    model = Product