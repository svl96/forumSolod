from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import Permission, User, Group
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
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


def send_reg_confirm(user):
    token = default_token_generator.make_token(user)
    title = 'Email confirm'
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    content = 'https://svl96.pythonanywhere.com/auth/valid/' + uid.decode() + '/' + token + '/'
    send_mail(title, content, 'sfiit@mail.ru', [user.email], fail_silently=False)


def logout(request):
    auth.logout(request)
    return redirect('/')


def confirm_user(request, uidb64, token):
    if uidb64 is not None and token is not None:
        uid = urlsafe_base64_decode(uidb64)
        try:
            user = User.objects.get(pk=uid)
            is_grouped = user.groups.all().filter(name='normalUser').exists()
            if default_token_generator.check_token(user, token) and not is_grouped:
                gr = Group.objects.get(name='normalUser')
                user.groups.add(gr)
        except:
            pass
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
            send_reg_confirm(authuser)
            return redirect('/')
        else:
            args['form'] = newuser
    return render(request, 'loginapp/reg.html', args)