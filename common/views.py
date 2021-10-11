from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, LoginForm, CustomUserChangeForm
from .models import User
from django.contrib.auth.decorators import login_required


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '비밀번호가 변경되었습니다')
            return redirect('/')
        else:
            messages.error(request, "에러 : 비밀번호가 변경이 안됐습니다")
    else:
        form = PasswordChangeForm(request.user)
        context = {'forms': form}
    return render(request, 'common/change_password.html', context)


@login_required
def delete(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            request.user.delete()
            auth_logout(request)
    return redirect('main:index')


@login_required
def update(request):
    context = {}
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(
            request.POST, instance=request.user)
        context = {'forms': user_change_form}
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('common:info', request.user.id)
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        context = {'forms': user_change_form}
    return render(request, 'common/update.html', context)


def info(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {'User': user}
    return render(request, 'common/info.html', context)


def login(request):
    loginform = LoginForm()
    context = {'forms': loginform}

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "GET":
        return render(request, "common/user_login.html", context)

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            auth_login(request, user)
            return redirect('main:index')

        else:
            print('인증실패')
    return render(request, "common/user_login.html", context)


def logout(request):

    auth_logout(request)
    return redirect('/')


def signup(request):
    """
    회원가입
    """
    context = {}

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            auth_login(request, user)  # 로그인
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'common/signup.html', {'forms': form})
