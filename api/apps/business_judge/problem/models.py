from django.utils.translation import ugettext_lazy as _
from django.db import models
from utils.models import BaseModel

from business_judge.description.models import Description


class Problem(BaseModel):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    max_score = models.FloatField(
        null=False
    )
    time_limit = models.FloatField(
        default=1.0
    )
    description = models.OneToOneField(
        Description,
        on_delete=models.CASCADE,
        related_name='problem',
        verbose_name=_(u'description')
    )
    # TODO - link?


class Tag(BaseModel):
    name = models.CharField(
        max_length=100
    )
    problem = models.ManyToManyField(
        Problem,
        on_delete=models.PROTECT,
        related_name='tag',
        verbose_name=_(u'problem')
    )
