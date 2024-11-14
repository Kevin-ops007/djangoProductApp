from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category, Tag


def index(request):
    return HttpResponse("Hello, world. You're at the product page.")


def product_list(request):
    """
    View that handles displaying a list of products with optional search and filtering by
    category and tags.

    Args:
        request: The HTTP request object with potential GET parameters for filtering:
            - q: Query string for searching product descriptions.
            - category: ID of the category for filtering.
            - tags: List of tag IDs for filtering.

    Returns:
        HttpResponse: Rendered HTML page displaying the filtered list of products,
        available categories, and tags.
    """
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
