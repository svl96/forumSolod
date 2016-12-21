from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import MyUserCreateForm, AuthForm
# Create your views here.


def login(request):
    args = dict()
    args['form'] = AuthForm()
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Неправильные логин/пароль'
            return render(request, 'loginapp/auth.html', args)
    else:
        return render(request, 'loginapp/auth.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


def reg(request):
    args = dict()
    args['form'] = MyUserCreateForm()
    if request.POST:
        newuser = MyUserCreateForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            authuser = auth.authenticate(username=newuser.cleaned_data['username'],
                                         password=newuser.cleaned_data['password1'])
            auth.login(request, authuser)
            return redirect('/')
        else:
            args['form'] = newuser
    return render(request, 'loginapp/reg.html', args)