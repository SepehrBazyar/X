from django.urls import path

from contents.views import CreatePostView


app_name = "contents"

urlpatterns = [
    path(
        "create/",
        CreatePostView.as_view(),
        name="create-post",
    ),
]
