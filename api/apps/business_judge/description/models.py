from django.db import models
from utils.models import BaseModel


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
    # TODO - Explanation in description?
