import hashlib
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from WaterApp.forms import StudentForm, QuestionsForm, RegistrationForm
from WaterApp.models import Accounts, Questions, Staff


def main(request):
    return render(request, 'main/base.html')


#@login_required
def index(request):
    template = 'poll/index.html'
    context = {'full_name': request.user}
    return render(request, template, context)


def accounts(request):
    return render(request, 'poll/AccountsManagement/accounts.dj.html')


def questions(request):
    return render(request, 'poll/QuestionsManagement/questions.dj.html')


def bulletin(request):
    if "id" in request.POST:
        print "@<<<<", request.POST, ">>>>"
        a = Accounts.objects.get(id=request.POST.get('id2'))
        print "@<<<<", request.POST.get('id2'), ">>>>"
        # print "@<<<<",request.POST.all(),">>>>"
        print "<<<<", a, ">>>>"
        if type(a) is not None:
            print a

            if "btn" in request.POST:
                btn = request.POST.get("btn")
                if btn == "search":
                    student_form = StudentForm({'id': a.id, 'last_name': a.last_name, 'first_name': a.first_name},
                                               instance=a)
                    print "Submit, Search"
                    if student_form.is_valid:
                        student_form.save(commit=False)
        else:
            student_form = StudentForm()
    else:
        # show a page without any post
        student_form = StudentForm()
    context = {'form': student_form}
    template = 'poll/PerformanceManagement/performance.dj.html'
    return render(request, template, context)


def user_management(request):
    return render(request, 'poll/AccountsManagement/AuthorizedUser/userManagement.html')


def create_student(request):
    student_form = StudentForm(request.POST or None)
    if student_form.is_valid:
        print "Account created"
        save_it = student_form.save(commit=False)
        save_it.user = request.user
        save_it.save()
    context = {"form": student_form}
    template = "poll/AccountsManagement/CreateStudent/createStudent.html"
    return render(request, template, context)


def update_student(request):
    if "id" in request.POST:
        print "@<<<<", request.POST, ">>>>"
        a = Accounts.objects.get(id=request.POST.get('id2'))
        print "@<<<<", request.POST.get('id2'), ">>>>"
        # print "@<<<<",request.POST.all(),">>>>"
        print "<<<<", a, ">>>>"
        if type(a) is not None:
            print a

            if "btn" in request.POST:
                btn = request.POST.get("btn")
                if btn == "search":
                    student_form = StudentForm({'id': a.id, 'last_name': a.last_name, 'first_name': a.first_name},
                                               instance=a)
                    print "Submit, Search"
                    if student_form.is_valid:
                        student_form.save(commit=False)

                elif btn == "update":
                    student_form = StudentForm(request.POST or None, instance=a)
                    print "Submit, Update"
                    if student_form.is_valid:
                        save_it = student_form.save(commit=False)
                        save_it.user = request.user
                        save_it.save()
                elif btn == "delete":
                    student_form = StudentForm(request.POST or None, instance=a)
                    print "Submit delete"
                    if student_form.is_valid:
                        delete_it = student_form.save(commit=False)
                        delete_it.user = request.user
                        delete_it.delete()
        else:
            student_form = StudentForm()
    else:
        # show a page without any post
        student_form = StudentForm()

    context = {"form": student_form}
    template = "poll/AccountsManagement/UpdateStudent/updateStudent.html"
    return render(request, template, context)


def update_user(request):
    if "username" in request.POST:
        a = Staff.objects.get(username=request.POST.get("username2"))
        if type(a) is not None:

            if "usr" in request.POST:

                usr = request.POST.get("usr")
                if usr == "search":
                    user_form = RegistrationForm(
                        {'username': a.username, 'password': a.password, 'last_name': a.last_name,
                         'first_name': a.first_name}, instance=a)
                    print "Submit, Search"
                    if user_form.is_valid:
                        user_form.save(commit=False)

                elif usr == "update":
                    user_form = RegistrationForm(request.POST or None, instance=a)
                    print "Submit, Update"
                    if user_form.is_valid:
                        save_it = user_form.save(commit=False)
                        save_it.user = request.user
                        save_it.save()
                elif usr == "delete":
                    user_form = RegistrationForm(request.POST or None, instance=a)
                    print "Submit delete"
                    if user_form.is_valid:
                        delete_it = user_form.save(commit=False)
                        delete_it.user = request.user
                        delete_it.delete()
        else:
            user_form = RegistrationForm()
    else:
        # show a page without any post
        user_form = RegistrationForm()

    context = {"form": user_form}
    template = "poll/AccountsManagement/AuthorizedUser/UpdateDeleteUser/updateDeleteUser.html"
    return render(request, template, context)


def create_user(request):
    user_form = RegistrationForm(request.POST or None)
    if 'password' in request.POST:
        hash_pw = hashlib.sha512(request.POST.get("password"))
        if user_form.is_valid:
            user_form = RegistrationForm({'username': request.POST.get('username'), 'password': hash_pw,
                                          'first_name': request.POST.get('first_name'),
                                          'last_name': request.POST.get('last_name')} or None)
            save_it = user_form.save(commit=False)
            save_it.save()
            user_form = RegistrationForm(None)
    else:

        print("aaaa")


    # user_form.password = hashlib.sha512(request.POST.get("password"))
    # save_it = user_form.save(commit=False)
    # save_it.user = request.user
    # save_it.save()

    context = {"form": user_form}
    template = 'poll/AccountsManagement/AuthorizedUser/CreateUser/createUser.html'
    return render(request, template, context)


def create_question(request):
    question_form = QuestionsForm(request.POST or None)
    if question_form.is_valid:
        save_it = question_form.save(commit=False)
        save_it.user = request.user
        save_it.save()
    context = {"form": question_form}
    template = 'poll/QuestionsManagement/CreateQuestion/createQuestion.html'
    return render(request, template, context)


def update_question(request):
    if "id" in request.POST:
        a = Questions.objects.get(id=request.POST.get("id2"))
        if type(a) is not None:
            if "btn" in request.POST:

                btn = request.POST.get("btn")
                if btn == "search":
                    questions_form = QuestionsForm({'id': a.id, 'question': a.question, 'option1': a.option1,
                                                    'option2': a.option2, 'option3': a.option3, 'option4': a.option4,
                                                    'answer': a.answer},
                                                   instance=a)
                    print "Submit, Search"
                    if questions_form.is_valid:
                        questions_form.save(commit=False)
                elif btn == "update":
                    questions_form = QuestionsForm(request.POST or None, instance=a)
                    print "Submit, Update"
                    if questions_form.is_valid:
                        save_it = questions_form.save(commit=False)
                        save_it.user = request.user
                        save_it.save()
                elif btn == "delete":
                    questions_form = QuestionsForm(request.POST or None, instance=a)
                    print "Submit delete"
                    if questions_form.is_valid:
                        delete_it = questions_form.save(commit=False)
                        delete_it.user = request.user
                        delete_it.delete()
        else:
            questions_form = QuestionsForm()
    else:
        # show a page without any post
        questions_form = QuestionsForm()

    context = {"form": questions_form}
    template = "poll/QuestionsManagement/UpdateQuestion/updateQuestion.html"
    return render(request, template, context)


# ----------------------------------------------------------------------
# ----------------|Question Schedule|-----------------------------------
def top_questions(request):
    latest_questions = Questions.objects.all().order_by("id")
    return [question in latest_questions]


def question_schedule(request):
    items = Questions.objects.all().order_by("id")
    context = {'items': items}
    template = 'poll/QuestionsManagement/QuestionSchedule/scheduleQuestions.html'
    return render(request, template, context)


# -----------------------------------------------------------------------
# -------------- |Authentication views| ---------------------------------
# -----------------------------------------------------------------------
"""
def login(request):

    c = {}
    c.update(csrf(request))
    auth_view(request)
    print "login"
    return render(request, "Main/Auth/login.html")
"""


def login(request):
    print 'login'
    if request.method == 'POST':
        print 'post'

        username = request.POST.get("username")
        password = request.POST.get("password")
        u = Staff.objects.get(username=username)
        print(">>>>", username, "|||", password, "<<<<")
        if type(u) is not None:
            print "=="

            bd_pw = u.password
            print "---", bd_pw
            if password == bd_pw:
                return HttpResponseRedirect('poll/index.html')

            else:
                return HttpResponseRedirect('Main/InvalidLogin')
        else:
            print '2222222'
            return HttpResponseRedirect('Main/InvalidLogin')
    return render(request, "Main/Auth/login.html")


def invalid_login(request):
    return render(request, 'Main/InvalidLogin/invalid_login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'poll/Logout/logout.html')


# ------------------------------------------------------------------------
'''
class StudentView(FormView):
    template_name = 'poll/AccountsManagement/accounts.dj.html'
    form_class = StudentForm

    def form_valid(self, student_form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        return super(StudentView, self).form_valid(student_form)


class StudentCreate(CreateView):
    model = Accounts
    fields = ['id', 'first_name', 'last_name']


class StudentUpdate(UpdateView):
    model = Accounts
    fields = ['first_name', 'last_name']
    template_name_suffix = '_update_form'


class DeleteStudent(DeleteView):
    model = Accounts
    success_url = reverse_lazy('student-list')

# -------------------------------------------------

class QuestionsView(FormView):
    template_name = 'poll/AccountsManagement/accounts.dj.html'
    form_class = QuestionsForm

    def form_valid(self, questions_form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        return super(QuestionsView, self).form_valid(questions_form)

class QuestionsCreate(CreateView):
    model = Questions
    fields = ['question', 'option1', 'option2', 'option3', 'option4', 'answer']


class QuestionsUpdate(UpdateView):
    model = Questions
    fields = ['question', 'option1', 'option2', 'option3', 'option4', 'answer']
    template_name_suffix = '_update_form'


class QuestionsStudent(DeleteView):
    model = Questions
    success_url = reverse_lazy('questions-list')

def create(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()

        return HttpResponseRedirect('/templates/index/index.html')
    else:
        form = StudentForm()
    args = {}
    args.update(csrf(request))

    args['forms'] = form

    return render_to_response(request, 'accounts.dj.html', args)'''
