from django.shortcuts import render, redirect
from .models import Proposal
from django.utils import timezone


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        response = request.POST.get("response")

        proposal = Proposal.objects.create(
            name=name, response=response, timestamp=timezone.now()
        )

        if response == "Yes":
            return redirect("yes_page", name=name)
        else:
            return redirect("no_page", name=name)

    return render(request, "index.html")


def yes_page(request, name):
    if request.method == "POST":
        email = request.POST.get("email")
        proposal = Proposal.objects.get(name=name)
        proposal.email = email
        proposal.save()
        return redirect("yes_page", name=name)
    return render(request, "yes_page.html", {"name": name})


def no_page(request, name):
    return render(request, "no_page.html", {"name": name})


def error(request):
    return redirect("index")
