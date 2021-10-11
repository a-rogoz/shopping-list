from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include("account.urls", namespace="account")),
    path('shopping_lists/', include("shopping_lists.urls", namespace="shopping_lists")),
    path('admin/', admin.site.urls),
]
