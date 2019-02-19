from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import BaseModel


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
    # TODO - link?

    def get_sample_test(self):
        return get_sample_test(
            problem=self
        )


from business_judge.test_case.selectors import (
    get_sample_test
)


class Tag(BaseModel):
    name = models.CharField(
        max_length=100
    )
    problem = models.ManyToManyField(
        Problem,
        related_name='tags',
        verbose_name=_(u'problem')
    )
