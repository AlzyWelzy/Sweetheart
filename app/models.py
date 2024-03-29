import uuid
from django.db import models
from django.contrib import admin
from django.utils import timezone


# Create your models here.
class Proposal(models.Model):
    user_identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    # response = models.CharField(
    #     max_length=5, choices=[("True", "Yes"), ("False", "No")]
    # )

    response = models.CharField(max_length=3)

    timestamp = models.DateTimeField(auto_now_add=True)

    email = models.EmailField(null=True, blank=True, max_length=254)

    def __str__(self):
        return f"{self.name} said {self.response} at {self.timestamp} on {self.email}"


admin.site.register(Proposal)
