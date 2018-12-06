from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import ListView, DetailView

# importing from .models
from .models import Product
from carts.models import Cart
from analytic.singnals import object_viewd_singnal
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

##########################################################################################
# passing cart to the context so that we can add product to the cart
# slug product section
class ProductSlugDetailView(DetailView):

    def get_context_data(self, *args, **kwargs):
        context = super(ProductSlugDetailView, self).get_context_data(*args, **kwargs)
        request = self.request
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context['cart'] = cart_obj
        return context

    #queryset = Product.objects.all()
    template_name = "products/product_detail.html"

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        request = self.request
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Product not exist")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("don't bother..")

        "for sending signals for analytics"
        #object_viewd_singnal.send(instance.__class__, instance=instance, request=request)
        return instance

# general product section
class ProductListView(ListView):
    # first way to manage list view
    #queryset = Product.objects.all()
    template_name = 'products/product_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        request = self.request
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


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
        return context

    #my custom query for retriving data in detailView
    def get_object(self, *args, **kwargs):
        #request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)  # my query
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
