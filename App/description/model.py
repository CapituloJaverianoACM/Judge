from django.db import models
from Judge.settings import FILE_ROOT, BASE_DIR


def directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    path = FILE_ROOT + f'test_cases/{instance.description.problem.id}/'
    return path

class Description(models.Model):
    statement = models.CharField(max_length=500, default="")
    input_format = models.CharField(max_length=500, default="")
    output_format = models.CharField(max_length=500, default="")
    # TODO como representar los ejemplos

    explanation = models.CharField(max_length=500, default="")


class TestCase(models.Model):
    name = models.CharField(max_length=100)
    fileIn = models.FileField(blank=False, null=False,
                              upload_to=directory_path)
    fileOut = models.FileField(blank=False, null=False,
                               upload_to=directory_path)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
