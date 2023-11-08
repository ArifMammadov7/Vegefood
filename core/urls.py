from django.conf.urls.static import static
from django.conf import settings
from django.urls import path #include,
from core import views
from core.views import *
from django.contrib import admin
from django.contrib.auth import views as auth_views
from social_django.urls import urlpatterns as social_auth_urls
# from django.conf.urls import static
# from core.urls import urlpatterns as core_urlpatterns 
# from views import home

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path ('blog/<slug:slug>/',detailblog,name='detailblog'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('search/', search, name="search"),
    path('wishlist/', views.wishlist, name='wishlist'), 
    path('shop/<slug:slug>/', views.detailproduct, name='detailproduct'),

   
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

