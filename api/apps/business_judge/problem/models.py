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

    def get_success_rate(self):
        return get_problems_with_success_rate(
            problem_id=self.id
        )[0].success_rate


from business_judge.test_case.selectors import (
    get_sample_test
)

from business_judge.problem.selectors import (
    get_problems_with_success_rate
)


class Tag(BaseModel):
    name = models.CharField(
        max_length=100
    )
    type = models.CharField(
        max_length=5
    )
    problem = models.ManyToManyField(
        Problem,
        related_name='tags',
        verbose_name=_(u'problem')
    )
