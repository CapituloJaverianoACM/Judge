VERDICT_CHOICES = (
    ('QUE', 'Queue'),
    ('JUD', 'Judging'),
    ('AC', 'Accepted'),
    ('WA', 'Wrong Answer'),
    ('TL', 'Time limit'),
    ('RTE', 'Run Time Error'),
    ('CE', 'Compilation Error'),
)

LANGUAGE_CHOICES = (
    ('PY3', 'Python3'),
    ('PY2', 'python2'),
    ('CPP', 'C++')
)


TIME_MAX_COMPILER = 5


COMMAND_COMPILER = {
    "PY3": "python -m py_compile ",
    "CPP": "g++ -std=c++11 -o files/{0} "
}

COMMAND_RUN = {
    "PY3": "python {0}",
    "CPP": "files/{1} "
}

EXTENSION = {
    "PY3": ".py",
    "CPP": ".cpp"
}
