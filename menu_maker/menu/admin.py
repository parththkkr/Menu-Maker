from django.contrib import admin
from .models import Category, Ingredient, Item, ItemIngredient, Menu, Order, OrderedItem

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Item)
admin.site.register(ItemIngredient)
admin.site.register(Order)
admin.site.register(OrderedItem)
admin.site.register(Menu)
