from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Log)
admin.site.register(Profile)
admin.site.register(Problem)
admin.site.register(Description)
admin.site.register(Submission)