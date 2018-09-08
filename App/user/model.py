from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    career = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # TODO como se va a colocar la imagenes?
    # TODO verificar los permisos bien
