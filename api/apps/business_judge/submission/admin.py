from business_judge.admin import judge_admin_site
from .models import Submission

judge_admin_site.register(Submission)
