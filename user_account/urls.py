from django.urls import path

from .views import (
    Register,
    Login,
    RetrieveUpdateDestroyUser
)


urlpatterns = [
    path("users/register/", Register.as_view()),
    path("users/login/", Login.as_view()),
    path("users/<int:id>/", RetrieveUpdateDestroyUser.as_view()),
]