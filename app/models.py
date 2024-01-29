from django.db import models
from django.contrib import admin


# Create your models here.
class Proposal(models.Model):
    name = models.CharField(max_length=255)
    # response = models.CharField(
    #     max_length=5, choices=[("True", "Yes"), ("False", "No")]
    # )

    response = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} said {self.response}"


admin.site.register(Proposal)
