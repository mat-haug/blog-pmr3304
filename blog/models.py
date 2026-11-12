from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField("título", max_length=200)
    content = models.TextField("conteúdo", help_text="Aceita código HTML.")
    date = models.DateTimeField("data de postagem", default=timezone.now)

    class Meta:
        ordering = ["-date"]
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
