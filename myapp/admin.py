from django.contrib import admin
from .models import ShoppingList, Inventory, Tag, ShoppingListTag


admin.site.register(ShoppingList)
admin.site.register(Inventory)
admin.site.register(Tag)
