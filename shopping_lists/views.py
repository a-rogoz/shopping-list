from django.http import request
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from .models import Product, ShoppingList
from .forms import ShoppingListForm
from django.forms import inlineformset_factory


# TODO Move some of the code to a separete class


@login_required
def shopping_lists_all(request):
    """
    Lists all shopping lists, which belong to the user.
    """
    return render(request, "home.html")


class ShoppingListCreate(View):
    """
    Creates a new shopping list and adds submitted products to it.
    """
    def get(self, *args, **kwargs):
        ProductFormSet = inlineformset_factory(ShoppingList, Product, fields=("product_name", "quantity"), extra=5, can_delete=False)
        return render(self.request, "shopping_lists/create.html", {"ProductFormSet": ProductFormSet})

    def post(self, *args, **kwargs):
        shopping_list_form = ShoppingListForm(self.request.POST)
        if shopping_list_form.is_valid():
            name = shopping_list_form.cleaned_data["name"]
            user = self.request.user
            
            try:
                new_shopping_list = ShoppingList()
                new_shopping_list.name = name
                new_shopping_list.user = user
                new_shopping_list.save()

                ProductFormSet = inlineformset_factory(ShoppingList, Product, fields=("product_name", "quantity"), extra=5, can_delete=False)
                formset = ProductFormSet(self.request.POST or None, instance=new_shopping_list)

                if formset.is_valid():
                    formset.save()
                return redirect('shopping_lists:shopping_lists_all')
            except ObjectDoesNotExist:
                return redirect('shopping_lists:shopping_lists_all')
        return redirect('shopping_lists:shopping_lists_all')


@login_required
def shopping_list_update(request, shopping_list_id):
    """
    Updates the shopping list and its products.
    """
    if request.method == "POST":
        shopping_list_form = ShoppingListForm(request.POST)
        if shopping_list_form.is_valid():
            name = shopping_list_form.cleaned_data["name"]
            
            try:
                shopping_list = ShoppingList.objects.get(pk=shopping_list_id)
                if (shopping_list.user.id == request.user.id):
                    updated_shopping_list = shopping_list
                    updated_shopping_list.name = name
                    updated_shopping_list.save()

                    ProductFormSet = inlineformset_factory(ShoppingList, Product, fields=("product_name", "quantity"), extra=5, can_delete=False)
                    formset = ProductFormSet(request.POST or None, instance=updated_shopping_list)

                    if formset.is_valid():
                        formset.save()
                    return redirect('shopping_lists:shopping_lists_all')
            except ObjectDoesNotExist:
                return redirect('shopping_lists:shopping_lists_all')
    else:
        try:
            shopping_list = ShoppingList.objects.get(pk=shopping_list_id)
            if (shopping_list.user.id == request.user.id):
                ProductFormSet = inlineformset_factory(ShoppingList, Product, fields=("product_name", "quantity"), extra=5, can_delete=False)
                formset = ProductFormSet(instance=shopping_list)
                return render(request, "shopping_lists/update.html", {"shopping_list": shopping_list, "formset": formset})
        except ObjectDoesNotExist:
            return redirect('shopping_lists:shopping_lists_all')


@login_required
def shopping_list_delete(request, shopping_list_id):
    """
    Deletes a shopping list by id.
    """
    try:
        shopping_list = ShoppingList.objects.get(pk=shopping_list_id)
        if (shopping_list.user.id == request.user.id):
            shopping_list.delete()
            return redirect('shopping_lists:shopping_lists_all')
        else:
            return redirect('shopping_lists:shopping_lists_all')
    except ObjectDoesNotExist:
        return redirect('shopping_lists:shopping_lists_all')


@login_required
def increase_product_quantity(request, shopping_list_id, product_id):
    """
    Increases the quantity by 1.
    """
    try:
        shopping_list = ShoppingList.objects.get(pk=shopping_list_id)
        product = Product.objects.get(pk=product_id)
        if (shopping_list.user.id == request.user.id):
            product.quantity = product.quantity + 1
            product.save()
            return redirect('shopping_lists:shopping_list_detail', shopping_list_id)
        else:
            return redirect('shopping_lists:shopping_lists_all')
    except ObjectDoesNotExist:
        return redirect('shopping_lists:shopping_lists_all')


@login_required
def decrease_product_quantity(request, shopping_list_id, product_id):
    """
    Decreases the quantity by 1.
    """
    try:
        shopping_list = ShoppingList.objects.get(pk=shopping_list_id)
        product = Product.objects.get(pk=product_id)
        if (shopping_list.user.id == request.user.id):
            if (product.quantity > 0):
                product.quantity = product.quantity - 1
                product.save()
            else:
                product.delete()
            return redirect('shopping_lists:shopping_list_detail', shopping_list_id)
        else:
            return redirect('shopping_lists:shopping_lists_all')
    except ObjectDoesNotExist:
        return redirect('shopping_lists:shopping_lists_all')


@login_required
def shopping_list_delete_product(request, shopping_list_id, product_id):
    """
    Deletes a product by id.
    """
    try:
        shopping_list = ShoppingList.objects.get(pk=shopping_list_id)
        product = Product.objects.get(pk=product_id)
        if (shopping_list.user.id == request.user.id):
            product.delete()
            return redirect('shopping_lists:shopping_list_detail', shopping_list_id)
        else:
            return redirect('shopping_lists:shopping_lists_all')
    except ObjectDoesNotExist:
        return redirect('shopping_lists:shopping_lists_all')


@login_required
def shopping_list_detail(request, shopping_list_id):
    """
    Displays a given shopping list by id.
    """
    try:
        shopping_list = ShoppingList.objects.select_related().get(pk=shopping_list_id)
    except ObjectDoesNotExist:
        return redirect('shopping_lists:shopping_lists_all')
        
    return render(request, "shopping_lists/detail.html", {"shopping_list": shopping_list})
