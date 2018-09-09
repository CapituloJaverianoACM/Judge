from django.db import models
from django.contrib.auth.models import User

'''
Rol
0 - admin
1 - user

'''


class Profile(models.Model):
    career = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # TODO verificar los permisos bien
    rol = models.IntegerField(default=1)
    # TODO como se va a colocar la imagenes?
