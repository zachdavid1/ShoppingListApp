

from django.shortcuts import get_object_or_404
from myapp.forms import TagForm
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import ShoppingList, Inventory, Tag, ShoppingListTag
from .forms import InventoryForm, TagForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal

@login_required
def get_shopping_list(request):

    limit = 5
    search_query = request.GET.get("search_query", "")
    items = ShoppingList.objects.filter(user = request.user)
    inventory_items = Inventory.objects.all()
    Tag_form = TagForm()
    tags = Tag.objects.filter(user_id = request.user)
    if search_query:
        inventory_items = inventory_items.filter(item_name__icontains=search_query)
        inventory_items = inventory_items[:limit]

    #calculate table values
    all_price = Decimal("0.00")
    bought_price = Decimal("0.00")
    not_bought_price = Decimal("0.00")

    tag_prices = {}
    for item in items:
        curr_price = item.quantity * item.item.item_price
        all_price += curr_price
        if item.checked:
            bought_price += curr_price
        else:
            not_bought_price += curr_price

        for shopping_list_tag in item.tags.all():
            tag = shopping_list_tag.tag_id
            if tag.id not in tag_prices:
                tag_prices[tag.id] = {
                    "name": tag.name,
                    "color": tag.color,
                    "all_price" : Decimal("0.00"),
                    "bought_price" : Decimal("0.00"),
                    "not_bought_price" : Decimal("0.00")
                }
            tag_prices[tag.id]["all_price"] += curr_price
            if item.checked:
                tag_prices[tag.id]["bought_price"] += curr_price
            else:
                tag_prices[tag.id]["not_bought_price"] += curr_price
            

    



    return render(request, 'myapp/shopping_list.html', {"items": items,"tags": tags, "TagForm": Tag_form, "inventory_items": inventory_items, 'bought_price': bought_price, 'all_price' : all_price, 'not_bought_price': not_bought_price, 'tag_prices': tag_prices.values()})

@login_required
def add_item(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(Inventory, id = item_id)
        if ShoppingList.objects.filter(user = request.user,item = item).exists():
            rep_item = ShoppingList.objects.get(user = request.user,item = item)
            rep_item_quantity = rep_item.quantity
            rep_item.quantity = rep_item_quantity + 1
            rep_item.save()
        else:
            ShoppingList.objects.create(
                user = request.user,
                item = item,
                quantity = 1

                )

 
        return redirect("get_shopping_list")
        
   

@login_required   
def delete_item(request, item_id):
    item = get_object_or_404(ShoppingList, id = item_id, user = request.user)
    item.delete()
    return redirect("get_shopping_list")

@login_required
def get_inventory_items(request):
    items = Inventory.objects.all()
    form = InventoryForm()
    return render(request, 'myapp/inventory.html', {'items': items, 'form': form})

@login_required
def toggle_item(request, item_id):
    if request.method == "POST":
        item = ShoppingList.objects.get(id = item_id, user = request.user)
        current_value = item.checked
        item.checked = not current_value
        item.save()
    return redirect('get_shopping_list')

@login_required
def clear_list(request):
    if request.method == 'POST':
        items = ShoppingList.objects.filter(user = request.user).delete()
    return redirect('get_shopping_list')

@login_required     
def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit = False)
            tag.user_id = request.user
            tag.save()
    return redirect('get_shopping_list')

@login_required
def delete_tag(request, tag_id):
    if request.method == 'POST':
        tag = Tag.objects.get(id = tag_id)
        tag.delete()
        return redirect('get_shopping_list')

@login_required
def add_to_inventory(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user_created=request.user
            item.is_global = False
            item.save()
    return redirect('inventory')

@login_required
def remove_from_inventory(request, item_id):
    if request.method == 'POST':
        item = Inventory.objects.get(id = item_id)
        item.delete()
    return redirect('inventory')


@login_required
def update_item_tag(request, item_id):
    if request.method == 'POST':
        list_item = ShoppingList.objects.get(user = request.user, id = item_id)
        action = request.POST.get("action")
        tag_id = request.POST.get("tag")
        if action == "clear":
            ShoppingListTag.objects.filter(list_item = list_item).delete()

        if tag_id:
            if action == "add":
                tag = Tag.objects.get(id = tag_id)
                ShoppingListTag.objects.get_or_create(
                    list_item = list_item,
                    tag_id = tag
                )
            elif action == "remove":
                ShoppingListTag.objects.filter(tag_id=tag_id, list_item = list_item).delete()
    return redirect('get_shopping_list')
        

@login_required
def update_quantity(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(ShoppingList, user = request.user, id = item_id)
        action = request.POST.get("action")
        quantity = item.quantity
        if action == 'add':
            item.quantity = quantity + 1
        elif action == 'minus':
            item.quantity = quantity - 1
        item.save()
        return redirect('get_shopping_list')
