from django.urls import path,re_path
from .views import (ProductListView, 
                            product_list_page, 
                            ProductDetailView, 
                            product_detail_page,
                            ProductFeaturedListView,
                            ProductFeaturedDetailView,
                            ProductSlugDetailView) 

apps_name = 'products'

urlpatterns = [
    # # prduct section
    
    # path('products-fbv/', product_list_page),
    # path('products/<int:pk>/', ProductDetailView.as_view()),
    # path('products-fbv/<int:pk>/', product_detail_page),

    # # product featured section
    # path('featured/', ProductFeaturedListView.as_view()),   
    # path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),   

    # product slug section
    path('<int:pk>/', ProductDetailView.as_view()),
    path('', ProductListView.as_view()),
    path('<slug>/', ProductSlugDetailView.as_view()),

]