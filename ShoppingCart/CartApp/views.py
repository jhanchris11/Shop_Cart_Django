from django.shortcuts import redirect, render
from CartApp.cart import Cart

from CartApp.models import Product

# Create your views here.
def tienda(request):
  products = Product.objects.all()
  return render(request,'shop.html',{'products':products})

def add_product(request,product_id):
  cart = Cart(request)

  product = Product.objects.get(id = product_id)
  # print('ga',product.object())
  # print(product.)
  cart.add(product)
  return redirect('Shop')

def delete_product(request,product_id):
  cart = Cart(request)
  product = Product.objects.get(id=product_id)
  cart.delete(product)
  return redirect('Shop')

def subtract_product(request,product_id):
  cart = Cart(request)
  product = Product.objects.get(id=product_id)
  cart.subtract(product)
  return redirect('Shop')
#request es nuestro session
def clean_cart(request):
  cart = Cart(request)
  cart.clean()
  return redirect('Shop')