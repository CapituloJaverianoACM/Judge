from urllib.error import HTTPError, URLError

from celery import shared_task
from django.db.models import QuerySet
import urllib
import os
import json

from business_judge.submission.selectors import get_submission_by_id
from business_judge.test_case.selectors import (
    get_output_file_by_id,
    get_input_file_by_id
)

@shared_task
def judge_submission(submission_id, host_address):
    host_address = 'http://' + host_address
    token = get_token(
        host_address=host_address
    )
    print(token)
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

def request(
        *,
        url,
        values,
        headers
):
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, headers)
    response=None
    try:
        response = urllib.request.urlopen(req)
    except HTTPError as e:
        # do something
        print('Error code: ', e.code)
        print("Error message:", e.msg)
    except URLError as e:
        # do something
        print('Reason: ', e.reason)
    else:
        # apply encoding constant utf-9
        response = response.read().decode('utf-8')
        response = json.loads(response)
        print('good!')
    return response

def get_path_by_binary_file(
        *,
        file
):
    pass


def get_source_code(
        *,
        submission
):
    pass


def get_input_path(
        *,
        test_case):
    pass


def get_output_path(
        *,
        test_case
):
    pass


def get_token(
        *,
        host_address: str
):
    print(host_address)
    url = host_address + '/api/login/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    values = {
        'username': os.environ.get('USERNAME_ADMIN_CELERY', 'admin'),
        'password': os.environ.get('PASSWORD_ADMIN_CELERY', 'admin')
    }
    response = request(
        url=url,
        values=values,
        headers=headers
    )
    print(response['token'])
    return "hi"


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

    source_code = get_source_code(
        submission=submission
    )
    print(source_code)
    # problem_id = get_problem_id(id, conn)[0]
    # problem = get_problem(problem_id, conn)
    time_limit = submission.problem.time_limit

    test_cases = submission.problem.test_cases.all()

    status = 'AC'

    for case in test_cases:
        fileIn = get_input_path(
            test_case=case
        )
        fileOut = get_output_path(
            test_case=case
        )
        print(fileIn)
        print(fileOut)
        '''
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

