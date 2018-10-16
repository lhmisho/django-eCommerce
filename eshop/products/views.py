from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import ListView, DetailView

# importing from .models
from .models import Product


# featured product section
class ProductFeaturedListView(ListView):
    # first way to manage list view
    #queryset = Product.objects.all()
    template_name = 'products/product_list.html'

    # another way to manage listView
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    # geting all object form Product
    queryset = Product.objects.all().featured()
    template_name = 'products/featured-detail.html'

    # another way to manage detail view
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


# general product section
class ProductListView(ListView):
    # first way to manage list view
    #queryset = Product.objects.all()
    template_name = 'products/product_list.html'
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

class ProductDetailView(DetailView):
    # geting all object form Product
    #queryset = Product.objects.all()
    template_name = 'products/product_detail.html'

    #my custom query for retriving data in detailView
    def get_object(self, *args, **kwargs):
        #request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)  # my query
        print(instance)
        if instance is None:
            raise Http404("product not found")
        return instance


def product_list_page(request):

    # getting data from products
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, 'products/product_list.html', context)

class ProductDetailView(DetailView):
    # geting all object form Product
    #queryset = Product.objects.all()
    template_name = 'products/product_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        print(context)
        return context

    #my custom query for retriving data in detailView
    def get_object(self, *args, **kwargs):
        #request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)  # my query
        print(instance)
        if instance is None:
            raise Http404("product not found")
        return instance

    # another way to manage detail view
    # def get_queryset(self, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)

def product_detail_page(request,pk=None, *args, **kwargs):
    # getting data from products
    # instance = Product.objects.get(pk=pk)
    # instace = get_object_or_404(Product, pk=pk)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print("Products doesn't exit")
    #     raise Http404("Product doesn't exist")
    # except:
    #     print("idiot go anyware else")

    # get_by_id is my custom query ... 
    instance   = Product.objects.get_by_id(pk)
    print(instance)
    if instance is None:
        raise Http404("product not found")

    # qs = Product.objects.filter(id=pk)
    # if qs.count() == 1:
    #     print(qs)
    #     instance = qs.first()
    # else:
    #     raise Http404("products doesn't exist")
    context = {
        'object' : instance
    }
    return render(request, 'products/product_detail.html', context)
