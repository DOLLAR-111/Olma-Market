from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from olma_app.models import Product, Cart


# Create your views here.
def main_page(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'index.html', context=context)


def note_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'detail.html', {'product': product})



@login_required(login_url='users:login')   
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    user = request.user   
    cart, created = Cart.objects.get_or_create(user=user, product=product)
    if created:
        cart.save()
    
    return redirect('home')   



@login_required(login_url='users:login')
def cart_list(request):
    user = request.user
    cart = Cart.objects.filter(user=user)   
    return render(request, 'cart.html', {'cart': cart})


@login_required(login_url='users:login')
def remove_from_cart(request, id):
    cart = get_object_or_404(Cart, id=id, user=request.user)    
    cart.delete()
    return redirect('cart-list')


from django.shortcuts import render
from .models import Product   

def search(request):
    query = request.GET.get('q')   
    results = Product.objects.filter(name__icontains=query) if query else []   

    return render(request, 'search_results.html', {
        'query': query,
        'results': results,
    })



def buy_product(request):
    return render(request, 'buy.html', {})