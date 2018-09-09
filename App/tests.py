from django.test import TestCase

# Create your tests here.


class DummyTest(TestCase):

    #   This is a dummy test to test Travis
    def test_travis(self):
        self.assertEqual('Hello', 'Hello')
