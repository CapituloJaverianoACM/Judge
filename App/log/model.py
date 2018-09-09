from django.db import models
from datetime import datetime


# TODO why logs?
class Log(models.Model):
    log = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(default=datetime.now, blank=True)
