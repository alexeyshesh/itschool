import uuid
from datetime import date, timedelta

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponse

from .models import *
from .forms import *


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
        if request.FILES.get('photo'):
            filepath = f'media/{me.username}_{uuid.uuid4()}'
            with open(filepath, 'wb+') as f:
                for chunk in request.FILES['photo'].chunks():
                    f.write(chunk)
        else:
            filepath = ''

        Post.objects.create(
            content=request.POST.get('content'),
            author=me,
            image_path=filepath,
        )

    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Пользователь @{username} не существует')

    if user != me:
        sub = Subscribe.objects.filter(subscriber=me, receiver=user).first()
    else:
        sub = None

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
        'subscribe': sub,
    }
    return render(request, 'main/user.html', context)


def subscribes(request, username: str, action: str):
    token = request.COOKIES.get('token')
    me = User.objects.filter(token=token).first()

    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Пользователь @{username} не существует')

    if action == 'subscribe':
        Subscribe.objects.create(
            subscriber=me,
            receiver=user,
        )
    elif action == 'unsubscribe':
        sub = (
            Subscribe.objects
            .filter(
                subscriber=me,
                receiver=user,
            )
            .first()
        )
        if sub is not None:
            sub.delete()
    else:
        return HttpResponseNotFound()

    return redirect(f'/{username}')


def news(request):
    token = request.COOKIES.get('token')
    me = User.objects.filter(token=token).first()

    subs = list(
        Subscribe.objects
        .filter(subscriber=me)
        .values_list('receiver', flat=True)
    )

    posts = list(
        Post.objects
        .filter(author__in=subs)
        .order_by('-created')
    )
    col_1 = posts[0::3]
    col_2 = posts[1::3]
    col_3 = posts[2::3]
    context = {
        'title': 'Новости',
        'me': me,
        'col_1': col_1,
        'col_2': col_2,
        'col_3': col_3,
    }
    return render(request, 'main/news.html', context)


def user_settings(request):
    token = request.COOKIES.get('token')
    me = User.objects.filter(token=token).first()

    if request.method == "POST":
        if request.FILES.get('avatar'):
            filepath = f'media/{me.username}_{uuid.uuid4()}'
            with open(filepath, 'wb+') as f:
                for chunk in request.FILES['avatar'].chunks():
                    f.write(chunk)
        else:
            filepath = ''

        me.first_name = request.POST.get('first_name') or me.first_name
        me.second_name = request.POST.get('second_name') or me.second_name

        if User.objects.filter(username=request.POST.get('username')) and me.username != request.POST.get('username'):
            return render(request, 'main/settings.html', {
                'user': me,
                'error': 'Пользователь с таким логином уже существует',
            })

        me.username = request.POST.get('username') or me.username
        me.avatar_path = filepath or me.avatar_path
        me.save()

        return redirect(f'/{me.username}')

    return render(request, 'main/settings.html', {'user': me})


def image(request, filename):
    with open(f'media/{filename}', 'rb') as f:
        return HttpResponse(content=f, content_type='image/jpeg')
