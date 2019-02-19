from business_judge.admin import judge_admin_site
from .models import Problem, Tag

judge_admin_site.register(Problem)
judge_admin_site.register(Tag)
