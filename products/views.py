from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy,reverse
# from django.core.urlresolvers import reverse
# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView,ListView
from Products.models import Product
from Products.forms import ProductForm


class ProductCreate(CreateView):
    form_class = ProductForm
    template_name="product/product.html"
    success_url = reverse_lazy('product-list')
    
    

class ProductUpdate(UpdateView):
    model = Product
    template_name="product/product.html"
    def get_success_url(self):
        return reverse("product-list")
    
    

class ProductDelete(DeleteView):
    model= Product
    template_name="product/product_confirm_delete.html"
    success_url = reverse_lazy('product-list')
   




class ProductDetailView(DetailView):
    model= Product
class ProductListView(ListView):
    queryset= Product.objects.all()
    template_name="product/index.html"