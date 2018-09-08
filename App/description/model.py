from django.db import models
from App.problem.model import Problem


class Description(models.Model):
    statement = models.CharField(max_length=500, default="")
    input_format = models.CharField(max_length=500, default="")
    output_format = models.CharField(max_length=500, default="")
    # TODO como representar los ejemplos

    explanation = models.CharField(max_length=500, default="")
    # TODO como representar los test cases

    problem = models.OneToOneField(
        Problem,
        on_delete=models.CASCADE
    )
