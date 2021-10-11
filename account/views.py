from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import RegisterForm


def account_register(request):
    """
    Registers a new user.
    """
    if request.user.is_authenticated:
        return redirect("shopping_lists:shopping_lists_all")

    if request.method == "POST":
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save()
            login(request, user)
            return redirect("shopping_lists:shopping_lists_all")
    else:
        registerForm = RegisterForm()
    return render(request, "account//register.html", {"form": registerForm})
