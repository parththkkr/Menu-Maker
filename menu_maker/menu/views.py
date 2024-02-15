from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from .models import Item, OrderedItem, User
from .forms import UserRegistrationForm, UserLoginForm
import json
from django.views.decorators.http import require_POST

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to home after successful registration 
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            raw_password = request.POST.get('password')
            user = User.objects.filter(username=username)
            if(user.first()):
                if(user.first().check_password(raw_password=raw_password)):
                    login(request, user.first())
                    return JsonResponse({'success': True})  # Return success response 
                else:                    
                    return JsonResponse({'error': 'Invalid credentials'}, status=400)
            else:
                return JsonResponse({'error': 'Invalid username'}, status=400)
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def list_items(request):
    items = Item.objects.all()  # Get all items
    return render(request, 'menu/list_items.html', {'items': items})

@login_required
def view_cart(request):
    user = request.user
    cart_items = OrderedItem.objects.filter(user=user, is_ordered=False)
    total_items = cart_items.count()
    total_cost = sum(item.itemObj.Price * item.quantity for item in cart_items)
    return render(request, 'menu/cart.html', {'cart_items': cart_items, 'total_items': total_items, 'total_cost': total_cost, 'user': user})

@login_required
@require_POST
def update_cart_item(request, item_id):
    user = request.user
    action = request.POST.get('action', '')
    cart_item = get_object_or_404(OrderedItem, id=item_id, user=user, is_ordered=False)

    if action == 'increase':
        cart_item.quantity += 1
        cart_item.save()
    elif action == 'decrease':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            # If the quantity is 1 and the user clicks "-", remove the item from the cart
            cart_item.delete()

    return redirect('view_cart')


@login_required
def apply_discount(request):
    discount_code = request.POST.get('discount_code', '')
    total_cost = float(request.POST.get('total_cost', 0))  # Ensure you're getting the correct key for total cost

    # Simple discount logic: 10% off for code "DISCOUNT10"
    if discount_code == 'DISCOUNT10':
        discount_amount = total_cost * 0.1
        total_cost -= discount_amount  # Deduct the discount amount from the total cost

    return render(request, 'menu/cart.html', {'total_cost': total_cost, 'discount_code': discount_code})



@login_required
def order_view(request):
    if request.method == 'POST':
        # Decode the raw byte data to extract JSON data
        data = json.loads(request.body.decode('utf-8'))
        item_id = data.get('item_id')

        # Assuming your logic to fetch item and user is correct
        user = request.user
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