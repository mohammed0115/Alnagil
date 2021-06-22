
from django.urls import path
from Products.views import (ProductDetailView,ProductDelete,
ProductListView,ProductUpdate,ProductCreate,ProductUpdate)

urlpatterns = [
    #...
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/delete/<int:pk>', ProductDelete.as_view(), name='product-delete'),
    path('products/create/', ProductCreate.as_view(), name='product-create'),
    path('products/update/<int:pk>', ProductUpdate.as_view(), name='product-update'),



]