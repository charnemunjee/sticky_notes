import os
from django.test import TestCase
from .models import Post
# Set the environment variable to your project's settings module

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sticky_notes.settings')


class PostTests(TestCase):
    def test_add_post(self):
        """Set up test data for Post model tests."""
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.'
        )

        self.post = Post.objects.create(
            title='Another Test Post',
            content='This is a another test post.'
        )

    def test_post_detail(self):
        """Test that the Post model has a title
        field and the title is correctly set."""
        self.test_add_post()  # Ensure that the test data is created
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'This is a test post.')

    def test_post_update(self):
        """Test that we can update a Post instance."""
        self.test_add_post()
        post = Post.objects.get(id=1)
        post.content = 'This is an updated test post.'
        post.save()
        self.assertEqual(post.content, 'This is an updated test post.')

    def test_post_delete(self):
        self.test_add_post()
        """Test that we can delete a Post instance."""
        sticky_note_count = Post.objects.count()
        post = Post.objects.get(id=1)
        post.delete()
        self.assertEqual(Post.objects.count(), sticky_note_count - 1)
