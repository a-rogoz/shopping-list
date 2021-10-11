import pytest
from pytest_factoryboy import register

from tests.factories import (
    ShoppingListFactory,
    ProductFactory,
)

register(ShoppingListFactory)
register(ProductFactory)


# TODO User Fixture


@pytest.fixture
def shopping_list(db, shopping_list_factory):
    shopping_list = shopping_list_factory.create()
    return shopping_list


@pytest.fixture
def product(db, product_factory):
    product = product_factory.create()
    return product