from django.shortcuts import redirect
from .models import Proposal
from django.utils import timezone
import uuid


def generate_user_identifier():
    return str(uuid.uuid4())


def create_proposal(name, response, user_identifier):
    return Proposal.objects.create(
        name=name,
        response=response,
        timestamp=timezone.now(),
        user_identifier=user_identifier,
    )


def update_proposal_email(proposal, email):
    proposal.email = email
    proposal.save()


def get_proposal_by_user_identifier(user_identifier):
    try:
        return Proposal.objects.get(user_identifier=user_identifier)
    except Proposal.DoesNotExist:
        return None


def get_proposal_or_redirect(request):
    user_identifier = request.session.get("user_identifier")

    if proposal := get_proposal_by_user_identifier(user_identifier):
        return proposal
    else:
        return redirect("error")
