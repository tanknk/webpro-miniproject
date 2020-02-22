from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, help_text="First name must less than 50 characters", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your First Name'}))
    last_name = forms.CharField(max_length=50, help_text="Last name must less than 50 characters", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Last Name'}))
    email = forms.EmailField(max_length=254, help_text="Email must be in the right format", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Username'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your Password'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your Password Again'}),
        # }
