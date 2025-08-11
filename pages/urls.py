from django.urls import path
from .views import (
    HomePageView, AboutPageView,
    ProductIndexView, ProductShowView,
    CartView, CartAddView, CartRemoveAllView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='products.index'),
    path('products/<int:id>/', ProductShowView.as_view(), name='products.show'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<int:product_id>/', CartAddView.as_view(), name='cart_add'),
    path('cart/removeAll/', CartRemoveAllView.as_view(), name='cart_removeAll'),
]
