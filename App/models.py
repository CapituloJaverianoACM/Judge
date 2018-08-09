import pytz
from django.db import models

from django.contrib.auth.models import User

#Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import exceptions

from datetime import datetime, timedelta

# Create your models here.

VEREDICT_CHOICES = (
    ('QUE', 'Queue'),
    ('JUD', 'Judging'),
	('AC', 'Accepted'),
	('WA', 'Wrong Answer'),
    ('TL', 'Time limit'),
    ('RTE', 'Run Time Error'),
    ('CE', 'Compilation Error'),
)

class Log(models.Model):
    log = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(default=datetime.now, blank=True)


class Profile(models.Model):
    career = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #TODO como se va a colocar la imagenes?
    #TODO verificar los permisos bien

class Description(models.Model):
    statement = models.CharField(max_length=500, default="")
    input_format = models.CharField(max_length=500, default="")
    output_format = models.CharField(max_length=500, default="")
    #TODO como representar los ejemplos

    explanation = models.CharField(max_length=500, default="")
    #TODO como representar los test cases

class Problem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    max_score = models.FloatField(null=True)
    difficulty = models.CharField(max_length=30, null=True)
    time_limit = models.FloatField(default=1.0)
    theme = models.CharField(max_length=100, default="")
    #TODO colocar bien el template
    template = models.CharField(max_length=500, default="")
    link_source = models.CharField(max_length=100, default="")
    is_original = models.BooleanField(default=False)
    #TODO verificar si la conexcion esta bien
    description = models.OneToOneField(Description, on_delete=models.CASCADE)

class Submission(models.Model):
    source_code = models.CharField(max_length=1000)
    veredict = models.CharField(max_length=4, choices=VEREDICT_CHOICES, default='QUE')
    #TODO verificar tipo de dato
    #score = models.DecimalField()

    time_stamp = models.DateTimeField(default=datetime.now, blank=True)
    #TODO verificar la eliminacino por cascade
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=200)
    problem_name = models.CharField(max_length=50)
    is_reply = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    # TODO verificar la eliminacino por cascade
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

class ExpiringTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid Token')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or delete')

        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)

        if token.created < utc_now - timedelta(hours=24):
            raise  exceptions.AuthenticationFailed('Token has expired')

        return token.user, token