from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet
from django.http import HttpResponse

from business_judge.test_case.models import (
    TestCaseModel,
    Problem
)


def get_sample_test(
        *,
        problem: Problem
) -> QuerySet:

    return TestCaseModel.objects.filter(
        problem=problem,
        is_sample=True
    )


def get_test_case_by_id(
        *,
        id: int
):
    test_case = TestCaseModel.objects.filter(
        id=id
    )
    if not test_case.exists():
        raise ValidationError("Test case not exists")
    return test_case[0]


def get_file_by_path(
        *,
        filename: str
):
    if not filename:
        raise ValidationError("Source code not exists")
    with open(filename, 'rb') as f:
        response = HttpResponse(f.read(),
                                content_type='application/x-www-form'
                                             '-urlencoded')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        response['Content-Type'] = 'application/x-www-form-urlencoded; ' \
                                   'charset=utf-8 '
        return response


def get_input_file_by_id(
        *,
        id: int
):
    test_case = get_test_case_by_id(
        id=id
    )
    filename = test_case.file_input.path
    return get_file_by_path(
        filename=filename
    )


def get_output_file_by_id(
        *,
        id: int
):
    test_case = get_test_case_by_id(
        id=id
    )
    filename = test_case.file_output.path
    return get_file_by_path(
        filename=filename
    )
