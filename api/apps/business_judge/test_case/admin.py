from business_judge.admin import judge_admin_site
from .models import TestCaseModel

judge_admin_site.register(TestCaseModel)
