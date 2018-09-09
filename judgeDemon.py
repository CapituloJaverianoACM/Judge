#!/usr/bin/python
import filecmp
import signal
import sqlite3
import subprocess
import threading
import time
from sqlite3 import Error
import os

BDPATH = 'db.sqlite3'
PATH_STATIC = './static/'

veredict_choices = ['QUE', 'JUD', 'AC', 'WA', 'TL', 'RTE', 'CE']


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def get_submission_queue(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM App_queuesubmission LIMIT 1")
    row = cur.fetchall()
    return row


def get_submission(id, conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM App_submission WHERE id = " + str(id))
    row = cur.fetchall()
    return row[0]


def get_problem(id, conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM App_problem WHERE id = " + str(id))
    row = cur.fetchall()
    return row[0]


def get_test_cases(id, conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM App_testcase WHERE description_id = " + str(id))
    rows = cur.fetchall()
    return rows


class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            print('Thread started')
            self.process = subprocess.Popen(self.cmd, shell=True,
                                            preexec_fn=os.setsid)
            self.process.communicate()
            print('Thread finished')

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            print('Terminating process')
            os.killpg(self.process.pid, signal.SIGTERM)
            thread.join()
            return (self.process.returncode, 4)
        return (self.process.returncode, 5)


def changue_state(id, conn, veredict):
    cur = conn.cursor()
    consulta = "UPDATE App_submission SET veredict = \'" + veredict_choices[
        veredict] + "\' WHERE id = " + str(id) + ";"
    cur.execute(consulta)
    cur.fetchall()
    conn.commit()


'''
status
2 - AC
3 - WA
4 - TL
5 - RTE
6 - CE
'''


def judge(id, conn):
    changue_state(id, conn, 1)
    submission = get_submission(id, conn)
    source_code = submission[1]
    problem_id = submission[5]
    problem = get_problem(problem_id, conn)
    time_limit = problem[4]
    test_cases = get_test_cases(problem[9], conn)
    status = 2
    for case in test_cases:
        fileIn = case[2]
        fileOut = case[3]
        os.system("echo --.-JOHAN--$ > " + PATH_STATIC + "out.out")
        os.system('chmod +x ' + source_code)
        command = source_code + ' < ' + fileIn
        command += ' > ' + PATH_STATIC + 'out.out'

        command_judge = Command(cmd=command)
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
                        status = 3
                        break
                    lineAc = fileAc.read()
                    lineVer = fileVer.read()
        if status != 2:
            break
    changue_state(id, conn, status)


def delete(id, conn):
    cur = conn.cursor()
    consulta = "DELETE FROM App_queuesubmission WHERE id = " + str(id) + ";"
    cur.execute(consulta)
    cur.fetchall()
    conn.commit()


def main():
    database = BDPATH

    # create a database connection
    conn = create_connection(database)
    with conn:
        while True:
            queue = get_submission_queue(conn)
            if not queue:
                print("Not submission in queue I go to sleep...  ")
                time.sleep(5)
                continue
            id = queue[0][1]
            queue_id = queue[0][0]
            judge(id, conn)
            delete(queue_id, conn)


if __name__ == '__main__':
    main()
