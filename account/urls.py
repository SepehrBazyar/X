from django.urls import path, include
from django.contrib.auth.views import (
    LoginView,
)

app_name = "account"

urlpatterns = [
    path(
        "my-login/",
        LoginView.as_view(),
        name="login-page",
    ),
]
