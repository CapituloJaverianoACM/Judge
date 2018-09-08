from django.db import models
from App.user.model import User
from App.problem.model import Problem

from datetime import datetime

VEREDICT_CHOICES = (
    ('QUE', 'Queue'),
    ('JUD', 'Judging'),
    ('AC', 'Accepted'),
    ('WA', 'Wrong Answer'),
    ('TL', 'Time limit'),
    ('RTE', 'Run Time Error'),
    ('CE', 'Compilation Error'),
)


class Submission(models.Model):
    source_code = models.CharField(max_length=1000)
    veredict = models.CharField(max_length=4, choices=VEREDICT_CHOICES,
                                default='QUE')
    # TODO verificar tipo de dato
    # score = models.DecimalField()

    time_stamp = models.DateTimeField(default=datetime.now, blank=True)
    # TODO verificar la eliminacino por cascade
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
