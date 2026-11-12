"""Versão 1: views funcionais, sem Django forms e sem validação de dados."""
from django.shortcuts import get_object_or_404, redirect, render

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"post_list": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def post_create(request):
    if request.method == "POST":
        post = Post.objects.create(
            title=request.POST["title"],
            content=request.POST["content"],
        )
        return redirect("blog:post_detail", pk=post.pk)
    return render(request, "blog/post_form.html", {})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.save()
        return redirect("blog:post_detail", pk=post.pk)
    return render(request, "blog/post_form.html", {"post": post})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("blog:post_list")
    return render(request, "blog/post_confirm_delete.html", {"post": post})
