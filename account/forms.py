from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    """
    Log in form.
    """
    username = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class RegisterForm(UserCreationForm):
    """
    Overides the built-in user registration form.
    """
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
	    user = super(RegisterForm, self).save(commit=False)
	    user.email = self.cleaned_data['email']
	    if commit:
		    user.save()
	    return user