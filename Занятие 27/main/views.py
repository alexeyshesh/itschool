import uuid
from datetime import date, timedelta

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound

from .models import *


def index(request):
    token = request.COOKIES.get('token')
    user = User.objects.filter(token=token).first()

    if user is None:
        return render(request, 'main/index.html')

    context = {
        'user_info': user,
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

        response = redirect('/')
        response.set_cookie('token', user.token)
        return response

    return render(request, 'main/login.html')


def logout(request):
    response = redirect('/')
    response.delete_cookie('token')
    return response


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
    if User.objects.filter(mail=data.get('mail')).first() is not None:
        raise Exception('Пользователь с такой почтой уже существует')
    if User.objects.filter(username=data.get('username')).first() is not None:
        raise Exception('Пользователь с таким логином уже существует')
    if len(data.get('birthday').split('.')) != 3 or len(data.get('birthday').split('.')[-1]) != 4:
        raise Exception('Введите дату в формате ДД.ММ.ГГГГ')


def reg(request):
    if request.method == 'POST':
        try:
            validate_reg(request.POST)

            birthday = request.POST.get('birthday')
            day, month, year = map(int, birthday.split('.'))
            birthday = date(year, month, day)
            if birthday >= date.today() - timedelta(365 * 13):
                raise Exception('Вы не можете зарегистрироваться, если вам меньше 13 лет')
        except Exception as e:
            context = {
                'error': e,
                'first_name': request.POST.get('first_name'),
                'second_name': request.POST.get('second_name'),
                'mail': request.POST.get('mail'),
                'username': request.POST.get('username'),
                'birthday': request.POST.get('birthday'),
            }
            return render(request, 'main/reg.html', context)

        User(
            username=request.POST.get('username'),
            first_name=request.POST.get('first_name'),
            second_name=request.POST.get('second_name'),
            mail=request.POST.get('mail'),
            password=request.POST.get('password'),
            token=str(uuid.uuid4()),
            birthday=birthday,
        ).save()
        return redirect('/')

    return render(request, 'main/reg.html')


def user(request, username: str):
    token = request.COOKIES.get('token')
    me = User.objects.filter(token=token).first()

    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Post.objects.create(
                author=me,
                content=content,
            )

    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Пользователь @{username} не существует')

    posts = list(Post.objects.filter(author=user).order_by('-created'))
    col_1 = posts[2::3]
    col_2 = posts[0::3]
    col_3 = posts[1::3]
    context = {
        'user': user,
        'me': me,
        'title': f'@{username}',
        'col_1': col_1,
        'col_2': col_2,
        'col_3': col_3,
    }
    return render(request, 'main/user.html', context)


def subscribe(request, username: str):
    token = request.COOKIES.get('token')
    me = User.objects.filter(token=token).first()

    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Пользователь @{username} не существует')

    Subscribe.objects.create(
        subscriber=me,
        receiver=user,
    )

    return redirect(f'/{username}')
