from django.contrib import admin
from App.user.model import Profile
from App.log.model import Log
from App.problem.model import Problem
from App.description.model import Description, TestCase
from App.submission.model import Submission, QueueSubmission

# Register your models here.
admin.site.register(Log)
admin.site.register(Profile)
admin.site.register(Problem)
admin.site.register(Description)
admin.site.register(Submission)
admin.site.register(QueueSubmission)
admin.site.register(TestCase)
