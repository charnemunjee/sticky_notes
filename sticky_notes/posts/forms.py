from .models import Post
from django import forms


# creates a form class with title and content fields
class PostForm(forms.ModelForm):
    """A form for creating and updating sticky notes instances."""
    class Meta:
        model = Post
        fields = ['title', 'content']
