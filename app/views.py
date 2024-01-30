from django.shortcuts import render, redirect
from .models import Proposal
from django.utils import timezone
import uuid


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        response = request.POST.get("response")

        user_identifier = str(uuid.uuid4())

        request.session["user_identifier"] = user_identifier

        proposal = Proposal.objects.create(
            name=name,
            response=response,
            timestamp=timezone.now(),
            user_identifier=user_identifier,
        )

        if response == "Yes":
            return redirect("yes_page")
        else:
            return redirect("no_page")

    return render(request, "index.html")


def yes_page(request):
    user_identifier = request.session.get("user_identifier")

    proposal = Proposal.objects.get(user_identifier=user_identifier)

    context = {
        "name": proposal.name,
    }

    print(context)
    if request.method == "POST":
        email = request.POST.get("email")

        proposal.email = email
        proposal.save()

    return render(request, "yes_page.html", context)


def no_page(request, name):
    user_identifier = request.session.get("user_identifier")

    proposal = Proposal.objects.get(user_identifier=user_identifier)

    context = {
        "name": proposal.name,
    }

    print(context)
    return render(request, "no_page.html", context)


def error(request):
    return redirect("index")
