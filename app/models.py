from django.db import models


# Create your models here.
class Proposal(models.Model):
    name = models.CharField(max_length=255)
    response = models.BooleanField()
