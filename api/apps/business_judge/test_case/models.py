from django.utils.translation import ugettext_lazy as _
from django.db import models
from utils.models import BaseModel

from business_judge.problem.models import Problem


# TODO - verify if the file save good

def directory_path_input(instance, filename):
    path = 'test_cases/{0}/input/{1}'\
        .format(
            instance.problem.id,
            instance.number
        )
    return path


def directory_path_output(instance, filename):
    path = 'test_cases/{0}/output/{1}'\
        .format(
            instance.problem.id,
            instance.number
        )
    return path


class TestCase(BaseModel):
    # TODO - get number
    number = models.IntegerField(
        default=0
    )
    file_input = models.FileField(
        blank=False,
        null=False,
        upload_to=directory_path_input
    )
    file_output = models.FileField(
        blank=False,
        null=False,
        upload_to=directory_path_output
    )
    explanation = models.CharField(
        max_length=500,
        default=""
    )
    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name='test_case',
        verbose_name=_(u'problem')
    )
