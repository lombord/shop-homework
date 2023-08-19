from django.urls import path

from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path("add-product", add_product, name='add_product'),
    path('product/<int:pk>/', check_product, name='product'),
    path('product/buy/<int:pk>/', buy_product, name='buy_product'),
    path('edit-product/<int:pk>/', edit_product, name='edit_product'),
    path('delete-product/<int:pk>/', delete_product, name='delete_product'),
    path('admin-page/', admin_page, name='admin_page'),
]
