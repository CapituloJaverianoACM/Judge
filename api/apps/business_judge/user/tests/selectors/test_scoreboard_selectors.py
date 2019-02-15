from django.test import TestCase
from django.contrib.auth.models import User

from business_judge.user.selectors import (
    get_scoreboard_general
)


class GetScoreboardGeneralTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="Test User")
        self.selector = get_scoreboard_general

    def test_get_scoreboard_general(self):
        # TODO - make
        pass
