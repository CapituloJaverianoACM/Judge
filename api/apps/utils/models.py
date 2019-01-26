from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    """
    Abstract class to help models.
    """
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_(u'created')
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_(u'updated')
    )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True

