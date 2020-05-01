from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path

from . import views

app_name ="main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("<single_slug>", views.single_slug, name="single_slug"),
    re_path(r'^signup/$', views.signup, name="signup"),
    re_path(r'^logout/$', views.logout_request, name="logout"),
    re_path(r'^login/$', views.login_request, name="login"),
]
