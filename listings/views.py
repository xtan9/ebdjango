from django.shortcuts import render
from . util import send_to_conversions_api

# Create your views here.
def index(request):
    print(request)
    print(request.META.get('REMOTE_ADDR'))
    #send_to_conversions_api(request)
    return render(request, 'listings/index.html')


def add_to_cart_1(request):
    return render(request, 'listings/add_to_cart_1.html')


def add_to_cart_2(request):
    return render(request, 'listings/add_to_cart_2.html')


def add_to_cart_3(request):
    return render(request, 'listings/add_to_cart_3.html')


def purchase(request):
    return render(request, 'listings/purchase.html')
