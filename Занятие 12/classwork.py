# Домашняя работа
# Задача 1

import re


def ispath(s):
    # Примеры путей:
    # C:\jjdn\vfvkj_12\name
    # /usr/isj
    return bool(re.match(r'\w:(/[\w\d_\-\.]+)+', s))

print(ispath('D:/dir1/dir2/file.txt'))
print(ispath('C:\\\\jjfns#'))


# Задача 2

def take_hashtags(s):
    return re.findall(r'#[\w\d_]+', s)


text = 'Всем привет! Сегодня сходил в кафе #VeganCafe и поел #булочку c #кофе. # # # ### text'
print(take_hashtags(text))

# Функциональное программирование

# нет переменных, только функции
# -> нет циклов
# функции являются объектами первого класса
# Примеры языков: Lisp (древний), Haskell

# Безопасность:

a = 4

def f():
    global a
    print('hello world')
    a = 3

print(a)
f()
print(a)

# Чтобы понять рекурсию, надо понять рекурсию
# n! = 1 * 2 * ... * n = 1 * 2 * ... (n-1) * n = (n-1)! * n
# 0! = 1

# Принципы написания рекурсивных функций
# 1. При написании функции считать, что функкция уже написана
# 2. Всегда должна быть нерекурсивная ветка
# 3. Данные должны меняться

def fact(n):
    if n == 0 or n == 1:
        return 1
    if n < 0:
        raise Exception('Factorial or neg number')
    return fact(n-1) * n


print(fact(5))
print(fact(0))
print(fact(20))

# Числа Фибоначчи
# 1 1 2 3 5 8 13 21 34 55 ...


def fibo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(5))
print(fibo(10))
print(fibo(20)/fibo(19)) # x^2 - x - 1 = 0

# функции - первоклассный объект

def decorate(f):
    print('Calling function')
    f()

def func():
    def g():
        return 'hello'
    print(g())

func()

# map - применяет функцию ко всем элементам списка

a = [1, 4, 2, 6, 7, 10]

def sqr(x):
    return x * x

b = list(map(sqr, a))
print(b)

# -> 7 2 30 4 5

# Пример использования map для считывания ввода:

i = input()
a1, a2, a3 = map(int, i.split())
print(a1, a2, a3)

# lambda - способ записи функций в одну строчку

a = [1, 4, 2, 6, 7, 10]
b = list(map(lambda x: x * x, a))
print(b)

# zip - из списков генерирует список кортежей

a = ['a', 'b', 'c']
b = [1, 2, 3, 4]
print(list(zip(a, b))) # -> [('a', 1), ('b', 2), ('c', 3)]

# генераторы - что-то между функцией и списком

def squares():
    i = 1
    while True:
        yield i * i  # yield - останавливает функцию и возращает результат
                     #         потом функкция выполняется с того же места
        i += 1

nums = [i for i in range(0, 10)]

g = squares()
for _ in range(10):
    print(next(g))  # next() используется для получения следующего значения генератора


