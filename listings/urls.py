from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_to_cart_1', views.add_to_cart_1, name='add_to_cart_1'),
    path('add_to_cart_2', views.add_to_cart_2, name='add_to_cart_2'),
    path('add_to_cart_3', views.add_to_cart_3, name='add_to_cart_3'),
    path('purchase', views.purchase, name='purchase')
]
