from django.shortcuts import render, redirect
from .utils import *


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        response = request.POST.get("response")

        user_identifier = generate_user_identifier()

        request.session["user_identifier"] = user_identifier

        proposal = create_proposal(name, response, user_identifier)

        return redirect("yes_page") if response == "Yes" else redirect("no_page")
    return render(request, "index.html")


def yes_page(request):
    proposal = get_proposal_or_redirect(request)

    context = {"name": proposal.name}

    if request.method == "POST":
        email = request.POST.get("email")

        update_proposal_email(proposal, email)

    return render(request, "yes_page.html", context)


def no_page(request):
    proposal = get_proposal_or_redirect(request)

    context = {"name": proposal.name}
    return render(request, "no_page.html", context)


def error(request):
    return redirect("index")
