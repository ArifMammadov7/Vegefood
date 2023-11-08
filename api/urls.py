from django.urls import path

from .views import *

urlspatterns=[
    path('shop/',ProductView.as_view(), name='Product'),
    path('Product/<int:id>/',ProductDetailApiView.as_view(),name='Product_detail'),
    path('subscriber/', SubsciberApiView.as_view(), name='subscriber'),
]

