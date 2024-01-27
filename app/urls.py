from django.urls import path, re_path
from .views import *

main_site = [
    path("", index, name="index"),
    re_path(r"^.*/$", error, name="error"),
]

urlpatterns = main_site
