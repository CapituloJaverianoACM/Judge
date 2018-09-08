from django.db import models
from App.description.model import Description


class Problem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    max_score = models.FloatField(null=True)
    difficulty = models.CharField(max_length=30, null=True)
    time_limit = models.FloatField(default=1.0)
    theme = models.CharField(max_length=100, default="")
    # TODO colocar bien el template
    template = models.CharField(max_length=500, default="")
    link_source = models.CharField(max_length=100, default="")
    is_original = models.BooleanField(default=False)
    # TODO verificar si la conexcion esta bien
    description = models.OneToOneField(Description, on_delete=models.CASCADE)
