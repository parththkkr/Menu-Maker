from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Item
from django.shortcuts import render, redirect
from .models import OrderedItem, Order, User
from .forms import OrderForm  # Import your order form if you have one
from django.http import HttpResponse
from django.db import connection
import json


# Existing views remain unchanged
def list_items(request):
    items = Item.objects.all()  # Get all items
    print(items)
    return render(request, 'menu/list_items.html', {'items': items})


def view_cart(request):
    user = User.objects.get(id=1)
    cart_items = OrderedItem.objects.filter(user=user, is_ordered=False)
    total_items = cart_items.count()
    total_cost = sum(item.itemObj.Price * item.quantity for item in cart_items)

    return render(request, 'menu/cart.html', {'cart_items': cart_items, 'total_items': total_items, 'total_cost': total_cost})

def apply_discount(request):
    discount_code = request.POST.get('discount_code', '')
    total_price = float(request.POST.get('total_price', 0))
    discount_amount = 0
    
    # Simple discount logic: 10% off for code "DISCOUNT10"
    if discount_code == 'DISCOUNT10':
        discount_amount = total_price * 0.1
        total_price *= 0.9

    return render(request, 'menu/cart.html', {'total_price': total_price, 'discount_amount': discount_amount})



def order_view(request):
    if request.method == 'POST':
        # Decode the raw byte data to extract JSON data
        data = json.loads(request.body.decode('utf-8'))
        item_id = data.get('item_id')

        # Assuming your logic to fetch item and user is correct
        user = User.objects.get(id=1)
        item = Item.objects.get(pk=item_id)
        cart_item = OrderedItem.objects.filter(itemObj=item, user=user, is_ordered=False).first()

        if cart_item:
            # If the item already exists in the cart, update the quantity by +1
            cart_item.quantity += 1
            cart_item.save()
        else:
            # If the item doesn't exist in the cart, create a new cart item with quantity 1
            cart_item = OrderedItem.objects.create(itemObj=item, user=user, quantity=1)

        
        return redirect('list_items')  # Redirect to a success page after ordering
    else:
        raise RuntimeError("No Page Found")
