from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
 path(
        "accounts/google/login/",
        LoginView.as_view(),
        name="login"
    ),
    path('profile/<str:name>/',ProfileView.as_view(),name='profile'),
]
