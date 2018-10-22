from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
# Create your views here.

class SearchProductView(ListView):
    # first way to manage list view
    #queryset = Product.objects.all()
    template_name = 'search/view.html'

    # passing request.GET.q as a query to the template
    def get_context_data(self, *args, **kwargs):
        request = self.request
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query   = request.GET.get('q')
        context['query'] = query
        return context


    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q',None)
        print(query)
        if query is not None:
            return Product.objects.search(query)  # using custom query from products.models
        return Product.objects.featured()