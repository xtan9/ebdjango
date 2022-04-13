from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('purchase', views.purchase, name='purchase')
]