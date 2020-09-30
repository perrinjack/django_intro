from django.test import TestCase

# Create your tests here.
import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question

""" TEST HELPERS
      Create a question with the given `question_text` and published the
      given number of `days` offset to now (negative for questions published
      in the past, positive for questions that have yet to be published).
      """


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=12)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_returns_question_text(self):
        recent_question = Question(question_text='First question')
        self.assertIs(recent_question.__str__(), 'First question')
