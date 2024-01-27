from django.shortcuts import render, redirect
from .models import Proposal


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        response = request.POST.get("response")

        Proposal.objects.create(name=name, response=response)

        if response == "Yes":
            return render(request, "yes_page.html", {"name": name})
        else:
            return render(request, "no_page.html", {"name": name})

    return render(request, "index.html")


def error(request):
    return redirect("index")
