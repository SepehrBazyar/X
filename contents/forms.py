from django import forms

from contents.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            "title",
        )

    def save(self, user, commit = ...):
        self.instance.author = user
        return super().save(commit)
