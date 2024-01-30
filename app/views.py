from django.shortcuts import render, redirect
from .models import Proposal
from django.utils import timezone
import uuid


def generate_user_identifier():
    # Generate a unique user identifier using UUID
    return str(uuid.uuid4())


def create_proposal(name, response, user_identifier):
    # Create a Proposal instance and save it to the database
    return Proposal.objects.create(
        name=name,
        response=response,
        timestamp=timezone.now(),
        user_identifier=user_identifier,
    )


def update_proposal_email(proposal, email):
    # Update the email field and save the proposal
    proposal.email = email
    proposal.save()


def get_proposal_by_user_identifier(user_identifier):
    # Try to get the Proposal associated with the user identifier
    try:
        return Proposal.objects.get(user_identifier=user_identifier)
    except Proposal.DoesNotExist:
        return None


def get_proposal_or_redirect(request):
    # Retrieve the user identifier from the session
    user_identifier = request.session.get("user_identifier")

    # Get the Proposal associated with the user identifier
    proposal = get_proposal_by_user_identifier(user_identifier)

    if proposal:
        return proposal
    else:
        # Handle the case where the Proposal does not exist
        return redirect("error")


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        response = request.POST.get("response")

        # Generate a unique user identifier
        user_identifier = generate_user_identifier()

        # Save the user identifier in the session
        request.session["user_identifier"] = user_identifier

        # Create a Proposal instance and save it to the database
        proposal = create_proposal(name, response, user_identifier)

        # Redirect based on the user's response
        if response == "Yes":
            return redirect("yes_page")
        else:
            return redirect("no_page")

    return render(request, "index.html")


def yes_page(request):
    proposal = get_proposal_or_redirect(request)

    context = {"name": proposal.name}

    if request.method == "POST":
        email = request.POST.get("email")

        # Update the email field and save the proposal
        update_proposal_email(proposal, email)

    return render(request, "yes_page.html", context)


def no_page(request):
    proposal = get_proposal_or_redirect(request)

    context = {"name": proposal.name}
    return render(request, "no_page.html", context)


def error(request):
    return redirect("index")
