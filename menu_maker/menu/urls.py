from django.urls import path
from . import views

urlpatterns = [
    # Existing URL patterns
    path('', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('cart/', views.view_cart, name='view_cart'),
    path('apply_discount/', views.apply_discount, name='apply_discount'),
    path('items/', views.list_items, name='list_items'),
    path('add/cart/', views.order_view, name='order_view'),
    # path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),



]
