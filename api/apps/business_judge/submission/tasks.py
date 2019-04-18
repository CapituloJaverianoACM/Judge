import pathlib
import shutil
import signal
import threading
import subprocess
from urllib.error import HTTPError, URLError

from celery import shared_task
from django.db.models import QuerySet
import urllib
import os
import json

from business_judge.submission.selectors import get_submission_by_id

from .constants import (
    TIME_MAX_COMPILER,
    COMMAND_COMPILER,
    COMMAND_RUN,
    EXTENSION
)


@shared_task
def judge_submission(submission_id, host_address):
    host_address = 'http://' + host_address
    token = get_token(
        host_address=host_address
    )
    print(token)
    judge_submission_process(
        submission_id=submission_id,
        host_address=host_address,
        token=token
    )
    return submission_id


def change_state_submission(
        *,
        submission,
        verdict: str
) -> None:
    '''
    Change the state of submission by de paramd verdict
    :param submission:
    :param verdict:
    :return: None
    '''
    submission.verdict = verdict
    submission.save()


def request(
        *,
        url,
        values,
        headers,
):
    data = None
    req = None
    if values:
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
        req = urllib.request.Request(url, data, headers=headers)
    else:
        req = urllib.request.Request(url, headers=headers)

    response = None
    try:
        response = urllib.request.urlopen(req)
    except HTTPError as e:
        # do something
        print('Error code: ', e.code)
        print("Error message:", e.msg)
        raise e

    except URLError as e:
        # do something
        print('Reason: ', e.reason)
        raise e
    else:
        # apply encoding constant utf-9
        response = response.read()
        print('good!')
    return response


def get_path_by_binary_file(
        *,
        file,
        name,
        ext
):
    pathlib.Path("files/").mkdir(
        parents=True,
        exist_ok=True
    )
    name = 'files/' + str(name) + ext
    f = open(name, "wb")
    f.write(file)
    f.close()
    return f.name


def get_source_code(
        *,
        submission_id,
        host_address,
        token,
        language
):
    url = host_address + \
        '/api/submissions/source_code/' + str(submission_id) + '/'
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': 'Token ' + str(token)}
    values = None
    response = request(
        url=url,
        values=values,
        headers=headers
    )
    path = get_path_by_binary_file(
        file=response,
        name=submission_id,
        ext=EXTENSION[language]
    )
    return path


def get_input_path(
        *,
        test_case,
        host_address,
        token
):
    url = host_address + '/api/test_cases/input/' + \
        str(test_case.id) + '/'
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': 'Token ' + str(token)}
    values = None
    response = request(
        url=url,
        values=values,
        headers=headers
    )
    path = get_path_by_binary_file(
        file=response,
        name=test_case.id,
        ext=".in"
    )
    return path


def get_output_path(
        *,
        test_case,
        host_address,
        token
):
    url = host_address + '/api/test_cases/output/' + \
        str(test_case.id) + '/'
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': 'Token ' + str(token)}
    values = None
    response = request(
        url=url,
        values=values,
        headers=headers
    )
    path = get_path_by_binary_file(
        file=response,
        name=test_case.id,
        ext=".out"
    )
    return path


def get_token(
        *,
        host_address: str
):
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
    response = response.decode('utf-8')
    response = json.loads(response)
    return response['token']


def clear_all(

):
    path = pathlib.Path("files/")
    shutil.rmtree(path)


class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            print('Thread started')
            self.process = subprocess.Popen(
                self.cmd,
                shell=True,
                preexec_fn=os.setsid
            )
            self.process.communicate()
            print('Thread finished')

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            print('Terminating process')
            os.killpg(self.process.pid, signal.SIGTERM)
            thread.join()
            return self.process.returncode, 4
        return self.process.returncode, 5


def judge_submission_process(
        *,
        submission_id,
        host_address,
        token
):
    '''
    Judge submission with specific id
    :param submission_id:
    :param host_address:
    :param token:
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

    language = submission.language

    source_code = get_source_code(
        submission_id=submission_id,
        host_address=host_address,
        token=token,
        language=language
    )
    print(source_code)
    # problem_id = get_problem_id(id, conn)[0]
    # problem = get_problem(problem_id, conn)
    time_limit = submission.problem.time_limit

    test_cases = submission.problem.test_cases.all()

    status = get_veredict(
        token=token,
        host_address=host_address,
        source_code=source_code,
        test_cases=test_cases,
        time_limit=time_limit,
        language=language,
        submission_id=submission_id
    )
    change_state_submission(
        submission=submission,
        verdict=status
    )
    print(status)


def get_veredict(
        *,
        test_cases,
        host_address,
        token,
        source_code,
        time_limit,
        language,
        submission_id
):
    status = "AC"

    print("Start with the os")

    os.system("echo --.-JOHAN--$  " + "out.out")
    # print(source_code)
    os.system('chmod +x ' + source_code)

    # Compiler process

    command = COMMAND_COMPILER[language].format(submission_id)
    command += source_code

    command_judge = Command(cmd=command)
    print(command)
    res = command_judge.run(timeout=TIME_MAX_COMPILER)

    print("Compiler get: ")
    print(res[0])

    compile_success = True

    if res[0]:
        status = "CE"
        compile_success = False

    for case in test_cases:
        if not compile_success:
            break

        # Get test case
        fileIn = get_input_path(
            test_case=case,
            host_address=host_address,
            token=token
        )
        fileOut = get_output_path(
            test_case=case,
            host_address=host_address,
            token=token
        )
        print(fileIn)
        print(fileOut)

        command = COMMAND_RUN[language].format(
            source_code,
            submission_id
        )

        command += ' < ' + fileIn

        command += ' > ' + 'files/out.out'

        command_judge = Command(cmd=command)
        print(command)
        res = command_judge.run(timeout=time_limit)

        if res[0]:
            status = "RTE"
            break

        with open(fileOut) as fileAc:
            with open("files/out.out") as fileVer:
                line_ac = fileAc.read()
                line_ver = fileVer.read()

                while line_ac or line_ver:
                    if line_ac.strip() != line_ver.strip():
                        status = "WA"
                        break
                    line_ac = fileAc.read()
                    line_ver = fileVer.read()
        if status != "AC":
            break

    clear_all()
    return status
