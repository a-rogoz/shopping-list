from .models import ShoppingList


def shopping_lists(request):
    """
    Attaches user's shopping lists.
    """
    user_id = request.user.id
    shopping_lists = ShoppingList.objects.filter(user=user_id)
    return {'shopping_lists': shopping_lists}