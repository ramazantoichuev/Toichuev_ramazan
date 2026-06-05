from django.urls import path
from .views import products_view, product_view, category_add_view, product_add_view, product_delete


urlpatterns = [
    path('', products_view, name='products'),
    path('products/<int:id>/', product_view, name='product'),
    path('categories/add/', category_add_view, name='create_category'),
    path('products/add/', product_add_view, name='add_product'),
    path('product/<int:id>/', product_delete, name='delete'),
]