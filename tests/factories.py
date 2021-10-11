import factory

from shopping_lists.models import (
    ShoppingList,
    Product
)
from faker import Faker

fake = Faker()


# TODO User Factory


class ShoppingListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShoppingList

    name = "Primary Shopping List"
    user = 1


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    shopping_list = factory.SubFactory(ShoppingListFactory)
    product_name = "product_title"
    quantity = "8"

