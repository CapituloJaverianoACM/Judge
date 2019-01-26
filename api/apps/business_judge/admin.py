from django.contrib.admin import AdminSite


class JudgeAdminSite(AdminSite):
    site_title = 'Judge'
    site_header = 'Judge administration'
    site_url = 'http://acm.javeriana.edu.co'


judge_admin_site= JudgeAdminSite(name='judge_admin')
