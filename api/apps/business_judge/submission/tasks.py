from celery import shared_task
from django.db.models import QuerySet

from business_judge.submission.selectors import get_submission_by_id


@shared_task
def judge_submission(submission_id):
    judge_submission_process(
        submission_id=submission_id
    )
    return submission_id


def change_state_submission(
        *,
        submission: QuerySet,
        verdict: str
) -> None:
    '''
    Change the state of submission by de paramd verdict
    :param submission:
    :param verdict:
    :return: None
    '''
    pass


def judge_submission_process(
        *,
        submission_id
):
    '''
    Judge submission with specific id
    :param submission_id:
    :return:
    '''
    submission = get_submission_by_id(
        id=submission_id
    )
    # TODO  - change verdict to a good constant
    change_state_submission(
        submission=submission,
        verdict='JUD'
    )

    source_code = submission.source_code
    print("source code " , source_code)
    # problem_id = get_problem_id(id, conn)[0]
    # problem = get_problem(problem_id, conn)
    time_limit = submission.problem.time_limit
    print("time limit " , time_limit)

    test_cases = submission.problem.test_cases
    print("test_cases " , test_cases)
    status = 'AC'
    '''

    for case in test_cases:
        fileIn = case[2]
        fileOut = case[3]
        os.system("echo --.-JOHAN--$ > " + PATH_STATIC + "out.out")
        # print(source_code)
        os.system('chmod +x ' + source_code)
        command = "python " + source_code + ' < ' + fileIn
        command += ' > ' + PATH_STATIC + 'out.out'

        command_judge = Command(cmd=command)
        # print(command)
        res = command_judge.run(timeout=time_limit)
        if res[0]:
            status = res[1]
            break

        with open(fileOut) as fileAc:
            with open(PATH_STATIC + 'out.out') as fileVer:
                lineAc = fileAc.read()
                lineVer = fileVer.read()
                while lineAc and lineVer:
                    if lineAc.strip() != lineVer.strip():
                        status = 'WA'
                        break
                    lineAc = fileAc.read()
                    lineVer = fileVer.read()
        if status != 2:
            break
    changue_state(id, , status)
    '''
