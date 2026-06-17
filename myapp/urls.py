from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.get_shopping_list, name = 'get_shopping_list'),
    path("add-item/<int:item_id>", views.add_item, name = 'add-item'),
    path("delete-item/<int:item_id>", views.delete_item, name = 'delete-item'),
    path("accounts/", include("allauth.urls")),
    path('toggle/<int:item_id>', views.toggle_item, name = 'toggle'),
    path('clear-list/', views.clear_list, name = 'clear-list'),
    path('create-tag/', views.create_tag, name = 'create-tag'),
    path('inventory/', views.get_inventory_items, name = 'inventory')  ,
    path('delete-tag/<int:tag_id>', views.delete_tag, name = 'delete-tag'),
    path ('add-to-inventory', views.add_to_inventory, name = 'add_to_inventory'),
    path('update-item-tag/<int:item_id>' ,views.update_item_tag, name='update_item_tag'),
    path('remove-from-inventory/<int:item_id>', views.remove_from_inventory, name = 'remove_from_inventory'),
    path('update-quantity/<int:item_id>', views.update_quantity, name = 'update_quantity')
 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)