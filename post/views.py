from django.http import Http404
from django.shortcuts import render, get_object_or_404
from post.models import Post

def render_post(request, post_id):
    p = get_object_or_404(Post, slug=post_id)
    return render(request, 'view_post.html', {'post': p})

def list_posts(request):
    posts = list(Post.objects.filter(public=True)[:10])
    if not posts:
        raise Http404
    return render(request, 'list_posts.html', {'posts': posts})
