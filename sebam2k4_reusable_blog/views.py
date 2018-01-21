# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
# Create your views here.

def post_list(request):
  print request
  '''
  Create a view that will return a list of Posts
  that were published prior to 'now'
  and render them to the 'blogposts.html' template
  '''
  # __lte is 'less-than-or-equal-to <='
  # -published_date indicates descending order
  posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
  return render(request, 'blogposts.html', {'posts': posts})

def post_detail(request, id):
  '''
  Create a view that returns a single Post object based
  on the post ID (pk) and render it to the 'postdetail.html'
  template. Or return a 404 error if the post is not found.
  '''
  post = get_object_or_404(Post, pk=id)
  post.views += 1 # clock up the number of post views
  post.save()
  return render(request, "postdetail.html", {'post': post})

def top_posts(request):
	"""
	Get a list of posts and order them
	by the number of views. Only return the
	top 5 results. Render it to blogposts.html
	"""
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')[:5]
	return render(request, "blogposts.html", {'posts': posts})

def new_post(request):
  '''
  A view that allows to create a new post.
  '''
  if request.method == "POST":
    # create instance of BlogPostForm and pass it to the blogpostform.html template
    form = BlogPostForm(request.POST, request.FILES) # BlogPostForm constructor w/ paremeters
    if form.is_valid():
      post = form.save(commit=False) # don't commit yet as need at least author details:
      post.author = request.user
      post.published_date = timezone.now()
      post.save()
      # Once form submitted and new blog post saved, redirect to the new blog
      # by passing in newly created post primary key
      return redirect(post_detail, post.pk)
  else:
    form = BlogPostForm() # instantiate (create table row)
  return render(request, 'blogpostform.html', {'form': form})

def edit_post(request, id):
  '''
  A view that allows us to edit a post that matched Post ID (pk)
  '''
  post = get_object_or_404(Post, pk=id)
  if request.method == "POST":
    form = BlogPostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.published_date = timezone.now()
      post.save()
      return redirect(post_detail, post.pk)
  else:
    form = BlogPostForm(instance=post) # instantiate (create table row)
  return render(request, 'blogpostform.html', {'form': form})