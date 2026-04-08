from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    """
    This function creates a view of all
    the sticky notes
    :param request: Description
    """
    posts = Post.objects.all()

    context = {
            'posts': posts,
            'page_title': 'list of sticky notes', }
    return render(request, 'posts/post_list.html', context)


def post_detail(request, pk):
    """
    This function displays the detail of a selected sticky note
    """
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


def post_create(request):
    """
    This function creates a new sticky note
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})


def post_update(request, pk):
    """
    This function updates an existing sticky note
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form})


def post_delete(request, pk):
    """
        This function deletes an existing sticky note
    """
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
