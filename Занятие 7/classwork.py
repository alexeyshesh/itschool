# Модули

# Чтобы использовать функции из модуля, его нужно импортировать с помощью import
# math - модуль с математическими функциями

import math
print(math.gcd(6, 9))

# os - модуль для работы с операционной системой
import os
print(os.listdir('venv'))

# если из модуля нужно не всё, можно импортироовать конкретную функцию
from math import sin
print(sin(5))

# Программы принято делить на модули, чтобы код был более понятным и читаемым
# Модуль - это обычный файл .py
# Если он лежит не в той же папке, указывается относительный путь через точки:

from modules.our_module import hello

# Классы - удобный сппособ организации и структурироования данных

# Удобно это потому что наборы данных, связанных с определенной задачей, и 
# функций для работы с ними, хранятся как будто бы в отдельных контейнерах
# и не перемешиваются

# print_phone_number()  # номер телефона
# print_car_number()  # номер машины

# Полиформизм - одна функция работает с разными типами данных
print(1)
print("hello")
print(True)

# Инкапсуляции - возможности скрыть часть данных - в python нет

# Наследоование, классы

# Пример: класс "прямоугольник"
x = 10
y = 10
point = (10, 10)


class Rect:
    def __init__(self, points):
        self.points = points
        self.p1 = points[0]
        self.p2 = points[1]

    def square(self):
        a = abs(self.p2[1] - self.p1[1])
        b = abs(self.p2[0] - self.p1[0])
        return a * b

    def perimeter(self):
        a = abs(self.p2[1] - self.p1[1])
        b = abs(self.p2[0] - self.p1[0])
        return (a + b) * 2

    def resize(self, points):
        self.points = points
        self.p1 = points[0]
        self.p2 = points[1]

    def __str__(self):
        a = abs(self.p2[1] - self.p1[1])
        b = abs(self.p2[0] - self.p1[0])
        s = ''
        for i in range(a):
            if i == 0 or i == a - 1:
                s += 'o' + '-' * (b - 2) + 'o\n'
            else:
                s += '|' + ' ' * (b - 2) + '|\n'
        return s


a = Rect([(0, 0), (10, 4)])
print(a)
a.resize([(0, 0), (5, 4)])
print(a)

# Пример: классы "животное" и "кот"

class Animal:
    def __init__(self):
        self.legs = 4
        self.hunger = 5

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 1
        else:
            self.hunger = 0


class Cat(Animal): # кот - это животное, то есть наследование - это уточнение
    amount = 0 # переменная общая для всех экземпляров класса
    def __init__(self, color='gray'):
        super().__init__()
        Cat.amount += 1  # считаем, сколько создано котов
        self.color = color

    def meow(self):
        print('meow')


cat = Cat()
cat1 = Cat()
cat2 = Cat()

print(Cat.amount)
