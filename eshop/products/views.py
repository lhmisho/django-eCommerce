from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

# importing from .models
from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context

def product_list_page(request):

    # getting data from products
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, 'products/product_list.html', context)

class ProductDetailView(DetailView):

    # geting all object form Product
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        print(context)
        return context

def product_detail_page(request,pk=None, *args, **kwargs):
    # getting data from products
    # instance = Product.objects.get(pk=pk)
    instace = get_object_or_404(Product, pk=pk)
    context = {
        'object' : instace
    }
    return render(request, 'products/product_detail.html', context)
