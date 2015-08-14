from django.test import TestCase
from WaterApp.models import Accounts, Questions

# Create your tests here.
class StudentTest(TestCase):
    # Test for Accounts class
    def test_str(self):
        student = Accounts(first_name="john", last_name="smith")

        self.assertEqual(str(student), 'john smith')


class QuestionsTest(TestCase):
    # test for Questions class
    def test_str(self):
        question = Questions(question="Capital of USA")
        option1 = Questions(option1="Miami")
        option2 = Questions(option2="Boston")
        option3 = Questions(option3="Washington")
        option4 = Questions(option4='Canada')
        answer = Questions(answer='Washington')

        self.assertEqual(str(question), 'Capital of USA')
        self.assertEqual(str(option1), 'Miami')
        self.assertEqual(str(option2), 'Boston')
        self.assertEqual(str(option3), 'Washington')
        self.assertEqual(str(option4), 'Canada')
        self.assertEqual(str(answer), 'Washington')
