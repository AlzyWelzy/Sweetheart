from django.urls import path
from .views import *

main_site = [
    path("", index, name="index"),
]

urlpatterns = main_site
