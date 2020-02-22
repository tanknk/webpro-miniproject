from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from post.models import Post, Message


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text_book', 'type', 'price', 'picture', 'status']
        widget={
        }

class MessageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Comment', 'style':'width:630px'}), label='')
    class Meta:
        model = Message
        fields = ['message']