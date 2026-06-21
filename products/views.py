from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(
        request,
        'products/product_list.html',
        {'products': products}
    )

@login_required
def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)

        product.quantity = quantity
        product.total_price = product.price * quantity

        total += product.total_price
        products.append(product)

    return render(
        request,
        'products/cart.html',
        {
            'products': products,
            'total': total
        }
    )



def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart

    print("CART =", cart)

    return redirect('product_list')



def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')


@login_required
def product_detail(request, id):
    product = Product.objects.get(id=id)

    return render(
        request,
        'products/product_detail.html',
        {'product': product}
    )

def checkout(request):
    return render(request, 'products/checkout.html')

def order_success(request):
    return render(request, 'products/order_success.html')