from itertools import count
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from posts.models import Post, Comment
from django.http import JsonResponse
import json
from django.db.models import Count
from posts.forms import CommentForm


# @login_required(login_url="login")
def home_page(request):
    if not request.user.is_authenticated:
        return redirect("login")  # Перенаправить на страницу логина

    all_posts = Post.objects.all()
    all_posts = Post.objects.annotate(
        likes_count=Count("liked_by"), comments_count=Count("comments")
    )

    for post in all_posts:
        post.short_caption = (
            post.caption[:30] + "..." if len(post.caption) > 30 else post.caption
        )

    current_user = request.user
    user_posts = Post.objects.filter(user=current_user)

    return render(
        request,
        "index.html",
        {
            "user_posts": user_posts,
            "all_posts": all_posts,
        },
    )


@login_required(login_url="login")
def liked_post(request):

    post_id = request.POST.get("post_id")
    post = get_object_or_404(Post, id=post_id)

    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
        liked = False
    else:
        post.liked_by.add(request.user)
        liked = True
    return JsonResponse({"liked": liked, "likes_count": post.liked_by.count()})


def comment_post(request, pk):
    user = request.user
    post = get_object_or_404(Post, id=pk)
    print(post.comments.all())
    comments = Comment.objects.filter(post=post)
    print(comments.count())
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("home")
    else:
        form = CommentForm

    return render(
        request,
        "comment_form.html",
        {
            "form": form,
            "post": post,
            "comments": comments,
        },
    )
