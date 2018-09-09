from django.db import models
from App.user.model import User
from App.problem.model import Problem
from Judge.settings import FILE_ROOT

from datetime import datetime


def directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    path = FILE_ROOT + f'submission/{instance.user.id}_{instance.problem.id}.py'
    return path




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
    veredict = models.CharField(max_length=4, choices=VEREDICT_CHOICES,                                default='QUE')
    score = models.FloatField(default=0.0)
    time_stamp = models.DateTimeField(default=datetime.now, blank=True)
    # TODO verificar la eliminacion por cascade
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    source_code = models.FileField(blank=False, null=False,
                                   upload_to=directory_path)


class QueueSubmission(models.Model):

    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
