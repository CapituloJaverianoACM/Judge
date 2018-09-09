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
    score = models.FloatField(default=0.0)

    time_stamp = models.DateTimeField(default=datetime.now, blank=True)
    # TODO verificar la eliminacion por cascade
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)


class QueueSubmission(models.Model):

    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
