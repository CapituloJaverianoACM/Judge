from celery import shared_task

@shared_task
def judge_submission():
    # TODO - judge
    return "ok"
