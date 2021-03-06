from django.db import models
from App.description.model import Description


class Problem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    max_score = models.FloatField(null=True)
    difficulty = models.IntegerField(default=1)
    time_limit = models.FloatField(default=1.0)
    theme = models.CharField(max_length=100, default="")
    # TODO colocar bien el template
    template = models.CharField(max_length=5000, default="")
    link_source = models.CharField(max_length=100, default="")
    is_original = models.BooleanField(default=False)
    description = models.OneToOneField(
        Description,
        on_delete=models.CASCADE
    )
