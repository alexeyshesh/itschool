import uuid
from datetime import date

from django.shortcuts import render, redirect

from .models import *


def index(request):
    token = request.COOKIES.get('token')
    user = User.objects.filter(token=token).first()

    if user is None:
        return render(request, 'main/index.html')

    context = {
        'user': user,
    }

    return render(request, 'main/index.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username, password=password).first()

        if user is None:
            context = {
                'error': 'Неправильный логин или пароль',
            }
            return render(request, 'main/login.html', context)

        if user.token == '':
            user.token = str(uuid.uuid4())
            user.save()

        response = render(request, 'success')
        response.set_cookie('token', user.token)
        return response

    return render(request, 'main/login.html')


def validate_reg(data):
    all_fields = True
    required_fields = [
        'username',
        'password',
        'password_again',
        'mail',
        'birthday',
        'first_name',
        'second_name',
    ]
    for field in required_fields:
        all_fields = all_fields and (field in data)

    if not all_fields:
        raise Exception('Не все поля заполнены')
    if data.get('password') != data.get('password_again'):
        raise Exception('Пароли не совпадают')
    if User.objects.filter(email=data.get('email')).first() is not None:
        raise Exception('Пользователь с такой почтой уже существует')
    if User.objects.filter(username=data.get('username')).first() is not None:
        raise Exception('Пользователь с таким логином уже существует')


def reg(request):
    if request.method == 'POST':
        try:
            validate_reg(request.POST)
        except Exception as e:
            context = {
                'error': e,
                'first_name': request.POST.get('first_name'),
                'second_name': request.POST.get('second_name'),
                'email': request.POST.get('email'),
            }
            return render(request, 'main/reg.html', context)

        birthday = request.POST.get('birthday')
        day, month, year = map(int, birthday.split('.'))
        birthday = date(year, month, day)

        User(
            username=request.POST.get('username'),
            first_name=request.POST.get('fist_name'),
            second_name=request.POST.get('second_name'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
            token=str(uuid.uuid4()),
            birthday=birthday,
        ).save()
        return redirect('/index')

    return render(request, 'main/reg.html')
