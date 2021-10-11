from django.urls import path

from .views import (
    shopping_lists_all,
    ShoppingListCreate,
    shopping_list_update,

    increase_product_quantity,
    decrease_product_quantity,
    shopping_list_delete_product,
    shopping_list_delete,

    shopping_list_detail
)

app_name = "shopping_lists"

urlpatterns = [
    path('', shopping_lists_all, name="shopping_lists_all"),
    path('create', ShoppingListCreate.as_view(), name="shopping_list_create"),
    path('<int:shopping_list_id>/update', shopping_list_update, name="shopping_list_update"),
    
    path('<int:shopping_list_id>/increase_quantity/<int:product_id>', increase_product_quantity, name="increase_product_quantity"),
    path('<int:shopping_list_id>/decrease_quantity/<int:product_id>', decrease_product_quantity, name="decrease_product_quantity"),
    path('<int:shopping_list_id>/delete_product/<int:product_id>', shopping_list_delete_product, name="shopping_list_delete_product"),
    path('<int:shopping_list_id>/delete', shopping_list_delete, name="shopping_list_delete"),
    
    path('<int:shopping_list_id>', shopping_list_detail, name="shopping_list_detail")
]
