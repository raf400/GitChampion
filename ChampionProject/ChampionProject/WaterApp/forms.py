from django import forms
from django.forms import ModelForm
from WaterApp.models import Accounts, Questions, Staff


class StudentForm(ModelForm):
    class Meta:
        model = Accounts
        fields = ['id', 'first_name', 'last_name']


class PerformanceForm(StudentForm):
    class Meta:
        widgets = {'id': 'disabled'}


class QuestionsForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['id', 'question', 'option1', 'option2', 'option3', 'option4', 'answer']


class UpdateQuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'answer']


class RegistrationForm(ModelForm):
    class Meta:
        model = Staff
        fields = ['username', 'password', 'first_name', 'last_name']
        widgets = {'password': forms.PasswordInput()}


# creates a form to add a student
# student_form = StudentForm()

# creates a form to add a questions
# question_form = QuestionsForm()

'''
# creates a form to update a student
 student = Accounts.objects.get(pk=1)
 form = StudentForm(instance=student)
'''
