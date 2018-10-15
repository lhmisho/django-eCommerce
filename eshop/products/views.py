from django.shortcuts import render
from django.views.generic import ListView, DeleteView

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
