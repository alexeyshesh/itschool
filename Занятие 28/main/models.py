from django.db import models
from django.utils.timezone import now


class User(models.Model):
    mail = models.CharField('E-mail', max_length=64)
    username = models.CharField('Логин', max_length=64)
    password = models.CharField('Пароль', max_length=64)
    first_name = models.CharField('Имя', max_length=64)
    second_name = models.CharField('Фамилия', max_length=64)
    birthday = models.DateField('Дата рождения')

    token = models.CharField('Токен', max_length=64, default='', blank=True)

    def __str__(self):
        return f'@{self.username}'


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    created = models.DateTimeField('Дата публикации', default=now)
    content = models.TextField('Содержание')
    image = models.ImageField('Фото', null=True, blank=True, default=None)

    def __str__(self):
        return f'@{self.author.username}: {self.content[:15]}...'


class Message(models.Model):
    created = models.DateTimeField('Дата отправки', default=now)
    is_read = models.BooleanField('Прочитано', default=False)
    sender = models.ForeignKey(User, related_name='Sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='Receiver', on_delete=models.CASCADE)
    content = models.TextField('Сообщение')

    def __str__(self):
        return f'@{self.sender.username} -> @{self.receiver.username} [{self.created}]'


class Subscribe(models.Model):
    subscriber = models.ForeignKey(User, related_name='Subscriber', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subscriber.username} -> {self.receiver.username}'
