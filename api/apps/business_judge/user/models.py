from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from utils.models import BaseModel
from .constants import UserRol


class Course(BaseModel):
    name = models.CharField(max_length=50)


class Profile(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    rol = models.IntegerField(
        choices=[
            (tag.value, tag)
            for tag in UserRol
        ],
        default=UserRol.USER.value
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name='profile',
        verbose_name=_(u'course')
    )
    # TODO - images
