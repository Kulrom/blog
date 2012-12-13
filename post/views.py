from django.shortcuts import render, get_object_or_404, get_list_or_404
from post.models import Post

def render_post(request, post_id):
	p = get_object_or_404(Post, slug=post_id)
	return render(request, 'view_post.html', {'post': p})

def list_posts(request):
	posts = get_list_or_404(Post, public=True)
	return render(request, 'list_posts.html', {'posts': posts})