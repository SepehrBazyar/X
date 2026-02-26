from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from contents.models import Post
from contents.forms import PostForm

# Create your views here.
class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "contents/create_post.html"
    success_url = reverse_lazy("home-page")
    # login_url = "http://127.0.0.1:8000/accounts/my-login/"

    def form_valid(self, form):
        print(self.request.user)
        self.object = form.save(
            user=self.request.user,
            commit=True,
        )
        return HttpResponseRedirect(self.get_success_url())
