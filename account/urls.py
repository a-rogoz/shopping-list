from django.contrib.auth import views as auth_views
from django.urls import path

from .views import account_register
from .forms import UserLoginForm


app_name = "account"

urlpatterns = [
    path("", auth_views.LoginView.as_view(template_name="account/login.html", form_class=UserLoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("register/", account_register, name="register"),
]
