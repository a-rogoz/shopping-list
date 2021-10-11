from django.db import models
from django.contrib.auth.models import User


class ShoppingList(models.Model):
    """
    The ShoppingList table contains all shopping lists created by users.
    """
    name = models.CharField(
        verbose_name="Name",
        help_text="Required",
        max_length=255
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="shopping_list_user"
    )
    created_at = models.DateTimeField(
        "Created at",
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        "Updated at",
        auto_now=True
    )

    class Meta:
        ordering = ("created_at",)
        verbose_name = "Shopping List"
        verbose_name_plural = "Shopping Lists"

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    The Product table holds each of the ShoppingList items.
    """
    product_name = models.CharField(
        verbose_name="Product",
        help_text="Required",
        max_length=255
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Quantity",
        help_text="Please specify quantity"
    )
    shopping_list = models.ForeignKey(
        ShoppingList,
        on_delete=models.CASCADE,
        related_name="shopping_list_product"       
    )
    created_at = models.DateTimeField(
        "Created at",
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        "Updated at",
        auto_now=True
    )

    class Meta:
        ordering = ("created_at",)
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name
