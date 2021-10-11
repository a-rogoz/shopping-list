from django import forms

from .models import Product, ShoppingList


class ShoppingListForm(forms.ModelForm):
    """
    Shopping List form
    """
    name = forms.CharField(
        min_length=3,
        max_length=255
    )

    class Meta:
        model = ShoppingList
        fields = ('name',)


class ProductForm(forms.ModelForm):
    """
    Product form
    """
    product_name = forms.CharField(
        label='Product Name',
        min_length=3,
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'})
    )
    quantity = forms.IntegerField(label='Quantity')

    class Meta:
        model = Product
        fields = ('product_name', 'quantity')




