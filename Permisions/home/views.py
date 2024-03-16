from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       SetPasswordForm, UserChangeForm,
                                       UserCreationForm)
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import AdminUserPrifoleForm, EditUserPrifoleForm, SignUp

# Create your views here.


def index(request):

    if request.method == 'POST':
        pass
    else:
        pass
    data = {}
    return render(request, "index.html", data)

def sign_up(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            messages.success(request, "Your account created succesfuly !!")
            # form.save() # save user only
            user = form.save()
            group = Group.objects.get(name='viewer') # adding user in to a group on Signup
            user.groups.add(group)
            form = SignUp()
    else:
        form = SignUp()
    data = {'form': form}
    return render(request, "signup.html", data)

def Log_in(request):
    mydata = {}
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login_form = AuthenticationForm(request=request, data=request.POST)
            if login_form.is_valid():
                uname = login_form.cleaned_data['username']
                upass = login_form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "You are successfuly login")
                    return HttpResponseRedirect("/dashboard/")
        else:
            login_form = AuthenticationForm()
        mydata = {'form': login_form}
        return render(request, "signin.html", mydata)
    else:
        return redirect("dashboard")


def dashboard(request):
    if request.user.is_authenticated:
        name = request.user
        data = {'name': name}
        return render(request, "dashboard.html", data)
    else:
        return redirect("login")


def log_out(request):

    logout(request)
    return redirect("login")
