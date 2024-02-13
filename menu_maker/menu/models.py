from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    CategoryName = models.CharField(max_length=255, default='Generic Category')

    def __str__(self):
        return self.CategoryName

class Ingredient(models.Model):
    IngredientName = models.CharField(max_length=255, default='Generic Ingredient')
    Quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.IngredientName

class Item(models.Model):
    ItemName = models.CharField(max_length=255, default='Generic Item')
    Description = models.TextField(default='No description available.')
    Price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    PreparationTime = models.IntegerField(null=True, blank=True, default=0)
    CategoryID = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.ItemName
    
    class Meta:
        db_table = "Items"

class OrderedItem(models.Model):
    itemObj = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_ordered = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add other fields like size, color, etc., as needed

    def __str__(self):
        return f"{self.quantity} x {self.itemObj.ItemName}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderedItem)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def total_cost(self):
        return sum(item.itemObj.Price * item.quantity for item in self.items.all())

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} - Total: ${self.total_cost()}"


class ItemIngredient(models.Model):
    ItemID = models.ForeignKey(Item, on_delete=models.CASCADE, default=1)
    IngredientID = models.ForeignKey(Ingredient, on_delete=models.CASCADE, default=1)

class Menu(models.Model):
    MenuName = models.CharField(max_length=255, default='Generic Menu')
    Description = models.TextField(default='No description available.')
    Price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Available = models.BooleanField(default=True)
    CreationDate = models.DateField(auto_now_add=True)
    CategoryID = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.MenuName
