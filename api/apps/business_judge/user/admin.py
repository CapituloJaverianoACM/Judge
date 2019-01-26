from business_judge.admin import judge_admin_site
from .models import Course, Profile

judge_admin_site.register(Course)
judge_admin_site.register(Profile)