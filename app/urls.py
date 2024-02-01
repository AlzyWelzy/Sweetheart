from django.urls import path, re_path
from .views import *

main_site = [
    path("", index, name="index"),
    path("yes/", yes_page, name="yes_page"),
    path("no/", no_page, name="no_page"),
    re_path(r"^.*/$", error, name="error"),
]

urlpatterns = main_site
