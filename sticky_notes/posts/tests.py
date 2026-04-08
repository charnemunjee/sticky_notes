import os
from django.test import TestCase
from django.urls import reverse
from .models import Post
# Set the environment variable to your project's settings module

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sticky_notes.settings')


class PostTests(TestCase):
    def setUp(self):
        """Set up test data for Post model tests."""
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.'
        )
        Post.objects.create(
            title='Another Test Post',
            content='This is a anothertest post.'
        )

    def test_post_has_title(self):
        """Test that the Post model has a title
        field and the title is correctly set."""
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Post')

    def test_post_has_content(self):
        """Test that the Post model has a
        content field and the content is correctly set."""
        post = Post.objects.get(id=1)
        self.assertEqual(post.content, 'This is a test post.')


class PostViewTests(TestCase):
    """Test the views for the Post model."""
    def setUp(self):
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.'
        )

    def test_post_list_view(self):
        """Test that the post list view returns a 200
        status code and contains the post title."""
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        """Test that the post detail view returns a 200
        status code and contains the post title and content."""
        post = Post.objects.get(id=1)
        response = self.client.get(reverse('post_detail', args=[str(post.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post.')
