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
            return redirect("yes_page", user_identifier=proposal.user_identifier)
        else:
            return redirect("no_page", user_identifier=proposal.user_identifier)

    return render(request, "index.html")


def yes_page(request, user_identifier):
    proposal = Proposal.objects.get(user_identifier=user_identifier)
    if request.method == "POST":
        email = request.POST.get("email")

        proposal.email = email
        proposal.save()

    return render(
        request, "yes_page.html", {"proposal": proposal, "name": proposal.name}
    )


def no_page(request, user_identifier):
    proposal = Proposal.objects.get(user_identifier=user_identifier)
    return render(
        request, "no_page.html", {"proposal": proposal, "name": proposal.name}
    )


def error(request):
    return redirect("index")
