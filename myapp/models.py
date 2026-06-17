
from django.db import models
from django.contrib.auth.models import User


class Inventory(models.Model):
    item_name = models.CharField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(default = None, blank = True, null=True)
    user_created = models.ForeignKey(User,on_delete=models.CASCADE)
    is_global = models.BooleanField(default = False)
    def __str__(self):
        return self.item_name

class ShoppingList(models.Model):
    quantity = models.IntegerField()
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE, null = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default = "")
    created_at = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default = False)

class Tag(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField()
    color = models.CharField(default = '#316813')

class ShoppingListTag(models.Model):
    list_item = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='tags')
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

