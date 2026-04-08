from django.urls import path
from .views import (
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete
    )

# URL patterns for to view, create, delete and update the sticky notes
urlpatterns = [
    # URL pattern for displaying a list of all posts
    path("", post_list, name="post_list"),

    # URL pattern for displaying details of a specific postcd
    path("post/<int:pk>/", post_detail, name="post_detail"),

    # URL pattern for creating a new post
    path("post/new/", post_create, name="post_create"),

    # URL pattern for updating an existing post
    path("post/<int:pk>/edit/", post_update, name="post_update"),

    # URL pattern for deleting an existing post
    path("post/<int:pk>/delete/", post_delete, name="post_delete"),
]
