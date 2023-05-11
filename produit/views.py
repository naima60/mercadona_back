from django.shortcuts import render
from produit.models import Produit
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    list_products = Produit.objects.filter(active='True')
    paginator = Paginator(list_products, 15) # 15 articles par page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'produit/index.html', context={'products': products})
