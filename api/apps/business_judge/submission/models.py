from django.utils.translation import ugettext_lazy as _
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from utils.models import BaseModel
from business_judge.problem.models import Problem
from .constants import VERDICT_CHOICES


def directory_submissions_path(instance, filename):
    path = 'submissions/{0}/{1}'\
        .format(
            instance.user.username,
            filename
        )
    return path


class Submission(BaseModel):
    verdict = models.CharField(
        max_length=4,
        choices=VERDICT_CHOICES,
        default='QUE'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='submission',
        verbose_name=_(u'user')
    )
    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name='submission',
        verbose_name=_(u'problem')
    )
    source_code = models.FileField(
        blank=False,
        null=False,
        upload_to=directory_submissions_path
    )
    cases_passed = models.IntegerField(
        default=0
    )

    def get_username(self):
        return self.user.username
