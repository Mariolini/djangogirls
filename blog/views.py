from django.shortcuts import redirect, render
import os.path

from blog.forms import PostForm
from .models import Post
from django.utils import timezone

def post_list(request):
    temppath = os.path.join('blog', 'post_list.html')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, temppath, {'posts':posts})

def post_detail(request, pk):
    temppath = os.path.join('blog', 'post_detail.html')
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    temppath = os.path.join('blog', 'post_edit.html')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, temppath, {'form': form})

def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})  