from django.shortcuts import render
from produit.models import Produit
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    list_products = Produit.objects.filter(active='True').order_by('id')
    paginator = Paginator(list_products, 15)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'produit/index.html', context={'products': products})
