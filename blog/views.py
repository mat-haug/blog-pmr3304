"""Versão 3: views com as classes genéricas do Django."""
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import PostForm
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"


class PostDetailView(DetailView):
    # DetailView já responde com 404 quando o post não existe.
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    # Após salvar, redireciona para Post.get_absolute_url().


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    context_object_name = "post"


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("blog:post_list")
