from django.shortcuts import render
from . util import send_to_conversions_api

# Create your views here.
def index(request):
    print(request)
    print(request.META.get('REMOTE_ADDR'))
    #send_to_conversions_api(request)
    return render(request, 'listings/index.html')


def add_to_cart(request):
    return render(request, 'listings/add_to_cart.html')


def purchase(request):
    return render(request, 'listings/purchase.html')
