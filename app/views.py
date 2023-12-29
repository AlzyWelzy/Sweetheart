from django.shortcuts import render, redirect
from .models import CrushResponse


def index(request):
    # if request.method == "POST":
    #     name = request.POST.get("name")
    #     response_value = request.POST.get("response")
    #     response = response_value == "True"
    #     CrushResponse.objects.create(name=name, response=response)

    #     if response:
    #         return render(request, "yes_page.html", {"name": name})
    #     return render(request, "no_page.html", {"name": name})

    return render(request, "index.html")
