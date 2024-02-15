from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class UserRegistrationForm(UserCreationForm):
    # Define any additional fields if needed
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))

