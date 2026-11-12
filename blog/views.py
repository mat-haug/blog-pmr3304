"""Views do blog: posts (classes genéricas), comentários e categorias."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import PostForm
from .models import Category, Comment, Post


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


class CommentCreateView(LoginRequiredMixin, CreateView):
    """Cria um comentário no post indicado pela URL; o autor é o usuário logado."""

    model = Comment
    fields = ["text"]
    template_name = "blog/comment_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.post_obj = get_object_or_404(Post, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = self.post_obj
        return context

    def form_valid(self, form):
        form.instance.post = self.post_obj
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.post_obj.get_absolute_url()


class CategoryListView(ListView):
    model = Category
    template_name = "blog/category_list.html"
    context_object_name = "category_list"


def category_detail(request, pk):
    """Lista os posts de uma categoria reutilizando o template de listagem de posts.

    Responde com 404 caso a categoria requisitada não exista.
    """
    category = get_object_or_404(Category, pk=pk)
    context = {
        "category": category,
        "post_list": category.posts.all(),
    }
    return render(request, "blog/post_list.html", context)
