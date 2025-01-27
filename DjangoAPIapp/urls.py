from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('categories',ListCategory.as_view(),name='categories'),
    path('categories/<int:pk>/',DetailCategory.as_view(),name='singlecategory'),
    
    path('books',ListBook.as_view(),name='book'),
    path('books/<int:pk>/',DetailBook.as_view(),name='singlebook'),
        
    path('products',ListProduct.as_view(),name='product'),
    path('products/<int:pk>/',DetailProduct.as_view(),name='singleproduct'),
]
