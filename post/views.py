from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from post.models import Post

def render_post(request, post_id):
    p = get_object_or_404(Post, slug=post_id)
    try:
        next_post = Post.objects.get(pk=(p.pk + 1))
    except ObjectDoesNotExist:
        next_post = None
    try:
        previous_post = Post.objects.get(pk=(p.pk - 1))
    except ObjectDoesNotExist:
        previous_post = None
    return render(request, 'view_post.html', {'post': p, 'next_post': next_post, 'previous_post': previous_post})

def list_posts(request):
    posts = list(Post.objects.filter(public=True)[:10])
    if not posts:
        raise Http404
    return render(request, 'list_posts.html', {'posts': posts})
