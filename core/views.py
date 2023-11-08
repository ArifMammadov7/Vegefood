from django.shortcuts import render,redirect
from django.http import HttpResponse,  HttpResponseRedirect
from django.urls import reverse
from core import forms
# Create your views here.   
from core.models import *
from core.forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    carousel_items = CarouselItem.objects.all()
    product = Product.objects.all()
    context={
        
        "x":Product.objects.all(),
        "x2":product[0:8],
        'carousel_items': carousel_items,
        "title": "Ana Səhifə ",
        'mentor':Testimonial.objects.all(),
     
    }
    return render(request, 'index.html', context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            form = ContactForm() 
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def about(request):
    context={
        'mentor':Testimonial.objects.all(),
        'about': About.objects.all()

    }
    return render(request, 'about.html', context)



def detailblog(request, slug):
    context={
      
        "blog": Blog.objects.get(slug=slug),

      
    }
    return render(request, 'blog-single.html', context)    



def blog(request):
    blog=Blog.objects.all()

    tag = Tag.objects.all()


    if "tag" in request.GET.keys():        
        blog = Blog.objects.filter(
            tag_id__title=request.GET["tag"])
    
    
    context={
       
        'blog': blog,
        'tag':tag
     
      
    }
    return render(request, 'blog.html', context=context)


def shop(request):
    category = Category.objects.all()
    products = Product.objects.all()


    if "category" in request.GET.keys():        
        products = Product.objects.filter(
            category_id__title=request.GET["category"])
    
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)
   
    context = {
        'page_obj': products,
        'mehsul': products,
        'category': category,
       
    }
    return render(request, 'shop.html', context)

def cart(request):
    context={

    }
    return render(request, 'cart.html', context)

def wishlist(request):
    context={
        "title": "Wish list"
    }
    return render(request, 'wishlist.html', context)



def detailproduct(request, slug):
    context={
      
        "product":Product.objects.get(slug=slug),

      
    }
    return render(request, 'productsingle.html', context)    


def search(request):
    
    query = request.GET.get('query')

    if query:
        products = Product.objects.filter(title__icontains=query)
      
        context = {
            'title': 'Search',
            'query': query,
            'products': products,
           
        }
        return render(request, 'search.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))
  