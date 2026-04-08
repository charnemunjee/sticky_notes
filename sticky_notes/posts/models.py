from django.db import models


# Created a Post model with:
# 1) title with max 100 characters
# 2) a text field
class Post(models.Model):
    """A model representing a sticky note post.
    The Post model has a title (with max 100 characters),
    content, and a created_at timestamp."""
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
