from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "categories"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 12}),
            "categories": forms.CheckboxSelectMultiple,
        }
