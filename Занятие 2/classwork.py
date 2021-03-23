"""
Функции

Любая программа - описание какого-то алгоритма. Иногда выполнять один и тот же 
алгоритм нужно много раз. Поэтому можно дать ему имя, как прееменной, и 
запускать по этому имени. Именно это и есть функции. Если алгоритм принимает 
какие-то входные данные, их можноо передать в качестве аргументов - как в 
математике. 

Описание функции выглядит так:

def <name>(<arg1>, <arg2>, ...):
    <code>
    return <result>

Вызов такой функции:

var = <name>(<arg1>, <arg2>, ...)

В переменной var будет лежать то, что функция вернула. Для того, чтобы вернуть 
значение используется ключевое слово return

"""

# Пример. Функция, которая здоровается - не возвращает результат

def say_hi(name):
    print("Hello, " + name)


say_hi("Ivan")

# Пример. Функция, определяющая, является ли число нечетным - возвращает либо
# True, либо False

def odd(number):
    return number % 2 == 1


print(odd(5), odd(6))


# Пример. функция с несколькими аргументами
# exl=True - аргумент exl по умолчанию равен True. Если у каких-тоо аргументов
# есть значения по умолчанию, их нужно указывать В КОНЦЕ

def greet(name, word, exl=True):
    if exl:
        words = word + " " + name + "!"
    else:
        words = word + " " + name
    print(words)


# При вызоове функции аргументы нужно передавать в том же порядке:
greet("Dmitry", "Hello", True)

# Если указано значение аргумента по умолчанию, его значение можно не указывать:
greet("Ivan", "Hi")

# Можно передавать аргументы в другом порядке, если явно указать, какой аргумент
# чему равен:
greet(exl=True, word="Hello", name="Dmitry")

# print - тоже функция. Она немного особенная, так умеет принимать сколько 
# угодно аргументов. При этом у нее есть два интересные аргумента:
# * sep=' ' - разделяет аргументы. Поэтому то, что мы хотим напечатать, 
#   выводится через пробел
# * end='\n' (\n - перенос строки) - то, что выведется в конце. По умолчанию это
#   перенос строки, поэтому каждый print печатает с новой строки

print("Hello", "Hi", "Good morning", sep=", ", end=".") # Hello, Hi, Good morning.

"""
Списки

a = [] - пустой список
b = [1, 5, 6]
c = [True, 'str', 3.4]

Нумерация элементов в списках идет с нуля. Чтобы обратиться к какому-то 
конкретному элементу испоользуются квадратныые скобки:

c[0] = False
print(c[1]) # str

Индексы могут быть отрицательными, тогда элементы берутся с конца c[-1] - 
последний элемент, c[-2] - предпоследний и так далее


len(c) - длина списка
c.append(<var>) - добавить что-то в конец списка
c.remove(<var>) - удалить значение из списка
"""

# Пример. Функция, которая считает сумму элементов списка

def list_sum(lst):
    s = 0
    i = 0
    while i < len(lst):
        s += lst[i]
        i += 1
    return s

print(list_sum([1, 4, 5, 8]))

# Пример. Функция, которая ищет максимальный элемент в списке

def list_max(lst):
    m = lst[0]
    i = 0
    while i < len(lst):
        if m < lst[i]:
            m = lst[i]
        i += 1
    return m

# Пример. Функция, которая ищет минимальный элемент в списке

def list_min(lst):
    m = lst[0]
    i = 0
    while i < len(lst):
        if m > lst[i]:
            m = lst[i]
        i += 1
    return m

# Можно не писать их каждый раз - они доступны из коробки: sum, max, min

lst = [3, 2, 5, 7, 1, 9]
print(sum(lst), min(lst), max(lst))

# Для сортировки списков есть функция sorted и метод sort
# sorted возвращает отсортированную копию списка, sort сортирует тот, для 
# которого вызывается

lst1 = sorted(lst, reverse=True) # по умолчанию сортировка по возрастанию, 
                                 # но если reverse=True, то наоборот
print(lst1)

# Для разворота списка аналогично используется метод reverse

lst1.reverse()


# Пример. Функция, определяющая индекс элемента, если он есть в списке, и 
# возвращающая -1, если его там нет

def list_find(lst, elem):
    i = 0
    while i < len(lst):
        if lst[i] == elem:
            return i
        i += 1
    return -1

print(list_find(lst, 6), list_find(lst, 10))

"""
Slice - способ взять часть списка

list[a:b:c] - часть списка list

* a - с какого индекса мы берем элементы. По умолчанию =0
* b - до какого индекса мы берем элементы. По умолчанию =-1
* с - с каким шагом мы берем элементы. По умолчанию =1
"""

# Примеры

lst = [4, 6, 3, 2, -1, 7, 7, 2, 5, 0]

print(lst[4:6])    # [-1, 7]
print(lst[4:])     # [-1, 7, 7, 2, 5, 0]
print(lst[:8])     # [4, 6, 3, 2, -1, 7, 7, 2]
print(lst[1:8:3])  # [6, -1, 2]
print(lst[8:3:-1]) # [5, 2, 7, 7, -1]
print(lst[8::-1])  # [5, 2, 7, 7, -1, 2, 3, 6, 4]
print(lst[::3])    # [4, 2, 7, 0]

# Решение задачи из ДЗ1 - посчитать сумму цифр числа

def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s


print(sum_digits(12345))