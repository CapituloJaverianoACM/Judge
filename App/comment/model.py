from django.db import models
from App.user.model import User
from App.problem.model import Problem

from datetime import datetime
 

class Comment(models.Model):
    content = models.CharField(max_length=200)
    problem_name = models.CharField(max_length=50)
    is_reply = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    # TODO verificar la eliminacino por cascade
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
