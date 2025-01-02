from django.shortcuts import redirect, render
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .models import Post


# Create your views here.
@login_required(login_url="login")
def post(request):

    form = PostForm
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "posts/post_form.html", {"form": form})


def edit_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            edit_form = form.save(commit=False)
            edit_form.user = request.user
            edit_form.save()
            return redirect("home")
    else:
        form = PostForm(instance=post)

    return render(request, "posts/edit_post.html", {"form": form})


def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect("home")
