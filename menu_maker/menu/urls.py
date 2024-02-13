from django.urls import path
from . import views

urlpatterns = [
    # Existing URL patterns
    path('', views.list_items, name='list_items'),  # Adjusted to serve as the home page
    path('cart/', views.view_cart, name='view_cart'),
    path('apply_discount/', views.apply_discount, name='apply_discount'),
    path('items/', views.list_items, name='list_items'),
    path('add/cart/', views.order_view, name='order_view'),

]
