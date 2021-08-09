from django.db import models


class Game(models.Model):
    title = models.CharField('Название', max_length=20)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class Report(models.Model):
    rate_choices = [
        (1, 'Очень плохо'),
        (2, 'Плохо'),
        (3, 'Нормальнно'),
        (4, 'Хорошо'),
        (5, 'Очень хорошо'),
    ]
    game = models.ForeignKey(Game, verbose_name='Игра', on_delete=models.CASCADE)
    text = models.TextField('Отзыв')
    rating = models.IntegerField('Оценка', choices=rate_choices)

    def __str__(self):
        return 'Отзыв о ' + self.game.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

