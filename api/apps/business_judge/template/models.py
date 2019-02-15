from django.utils.translation import ugettext_lazy as _
from django.db import models
from utils.models import BaseModel

from business_judge.problem.models import Problem


class Template(BaseModel):
    code = models.CharField(
        max_length=5000,
        default=""
    )
    problem = models.ManyToManyField(
        Problem,
        on_delete=models.PROTECT,
        related_name='template',
        verbose_name=_(u'problem')
    )
