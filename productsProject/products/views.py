from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category, Tag


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def product_list(request):
    products = Product.objects.all()
    query = request.GET.get("q")
    category_id = request.GET.get("category")
    tag_ids = request.GET.getlist("tags")

    if query:
        products = products.filter(description__icontains=query)
    if category_id:
        products = products.filter(category_id=category_id)
    if tag_ids:
        products = products.filter(tags__id__in=tag_ids).distinct()

    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(
        request,
        "products/product_list.html",
        {
            "products": products,
            "categories": categories,
            "tags": tags,
        },
    )
