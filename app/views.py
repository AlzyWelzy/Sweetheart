from django.shortcuts import render, redirect
from .models import Proposal


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        response_value = request.POST.get("response")
        response = response_value == "True"
        print(name, response)
        Proposal.objects.create(name=name, response=response)

        if response:
            return render(request, "yes_page.html", {"name": name})
        else:
            return render(request, "no_page.html", {"name": name})

    return render(request, "index.html")
