from django.utils.translation import ugettext_lazy as _
from django.db import models
from utils.models import BaseModel

from business_judge.problem.models import Problem

class Description(BaseModel):
    statement = models.CharField(
        max_length=1500,
        default=""
    )
    input_format = models.CharField(
        max_length=500,
        default=""
    )
    output_format = models.CharField(
        max_length=500,
        default=""
    )
    problem = models.OneToOneField(
        Problem,
        on_delete=models.CASCADE,
        related_name='description',
        verbose_name=_(u'problem')
    )
    # TODO - Explanation in description?
