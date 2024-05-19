from django.shortcuts import render
from testapp import forms
# to add login : provided by django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def home_view(request):
    return render(request, 'testapp/home.html')

@login_required
def java_exam_view(request):
    return render(request, 'testapp/java.html')

@login_required
def python_exam_view(request):
    return render(request, 'testapp/python.html')

@login_required
def apti_exam_view(request):
    return render(request, 'testapp/apti.html')


def logout_view(request):
    return render(request, 'testapp/logout.html')


def signup_views(request):
    #get
    form = forms.SignUpForm()
    #post
    if request.method =='POST':
        form = forms.SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'testapp/signup.html', {'form': form})

# http://127.0.0.1:8000/accounts/login/?next=/java/