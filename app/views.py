from django.shortcuts import render, redirect
from .models import Proposal
from django.utils import timezone


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        response = request.POST.get("response")

        Proposal.objects.create(name=name, response=response, timestamp=timezone.now())

        if response == "Yes":
            return render(request, "yes_page.html", {"name": name})
        else:
            return render(request, "no_page.html", {"name": name})

    return render(request, "index.html")


def error(request):
    return redirect("index")
