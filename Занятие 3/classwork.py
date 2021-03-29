# Разбор ДЗ

# 2

i = 0
numbers = []
while i < 5:
    numbers.append(int(input()))
    i += 1

numbers.sort(reverse=True)
print(numbers)

# 3

def day2date(day):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    s = 0
    i = 0
    while s + months[i] < day:
        s += months[i]
        i += 1

    print(month_name[i], day - s)

day2date(365)

# 4

def pifagor(a, b):
    return (a * a + b * b) ** 0.5

print(pifagor(3, 4))

# 5

def is_pal(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10

    # 1 способ
    digits1 = digits.copy()
    digits1.reverse()
    
    return digits == digits1

    # 2 способ
    pal = True
    
    i = 0
    while i < len(digits) // 2:
        if digits[i] != digits[-1-i]:
            pal = False
        i += 1
    
    return pal

print(is_pal(1234))
print(is_pal(12321))


# оператор in: <elem> in <list> - проверка того, что <elem> есть в списке <list>

user_ids = [123, 456, 432]
id = int(input())
if id in user_ids:
    print('Welcome')
else:
    print('You are not in user list')


"""
Цикл for - способо перебирать элементы списка

for <obj> in <iter>:
    <code>
"""

names = ['Ivan', 'Oleg', 'Anna']

for name in names:
    if name == 'Oleg':
        print(name, ' gde maket')
    else:
        print('Hello,', name)

# Примеры

numbers = [1, 5, 4, 3, 6, 7, 8, 9, 7, 4]

# Посчитать количество четных чисел в списке

s = 0
for number in numbers:
    if number % 2 == 0:
        s += 1

print(s)

# Посчитать сумму элементов списка

s = 0
for number in numbers:
    s += number

print(s)

# range(a, b, c) - генерирует список от a до b-1 с шагом c
# Сумма нечетных чисел от 1 до n

n = int(input())

s = 0
for i in range(1, n + 1, 2):
    s += i

print(s)


# Составить список разностей элементов списка следующего с предыдущим
diffs = []
for i in range(1, len(numbers)):
    diffs.append(numbers[i] - numbers[i - 1])

print(diffs)


# Можно использовать не весь список, а его часть
for n in numbers[0:5]:
    print(n)

# Вывести квадраты чисел от 1 до n
# 1 4 9 16 25

n = int(input())

for i in range(n + 1):
    print(i * i)



# Оператор break - экстренно останавливает работу цикла
# Оператор continue - переходит к следующей итерации цикла
# Пример. Читать числа либо до 0, максимум пять чисел

amount = 0
n = 1
lst = []

while amount < 5:
    n = int(input())
    if n == 0:
        break
    lst.append(n)
    amount += 1

# Пример. Читать числа либо до 0, максимум пять чисел, десятки в список не добавлять

amount = 0
n = 1
lst = []

while amount < 5:
    n = int(input())
    if n == 0:
        break
    if n == 10:
        continue
    lst.append(n)
    amount += 1


# Считывать команды, пока не придет кооманда exit
while True:
    cmd = input()
    if cmd == 'exit':
        break


# Списочные выражения - способ создавать списки с ппомощью цикла for в одну строку
# Просто - [f(elem) for elem in list]
# С условием (брать не все элементы из list) - [f(elem) for elem in list if <cond>]
# Обработка в зависимости от условия - [f(elem) if <cond> else g(elem) for elem in list]

# Пример. Создать список квадратов чисел от 1 до n

n = int(input())
sqrs = [i * i for i in range(1, n+1)]
sqrs1 = [elem % 3 for elem in sqrs]
print(sqrs, sqrs1)


numbers = [1, 5, 4, 3, 6, 7, 8, 9, 7, 4]
# только четные числа из numbers
even_numbers = [n for n in numbers if n % 2 == 0] 
# числа из numbers, если четное - оставляем так, если нечетное - прибавить единицу
all_even_numbers = [n if n % 2 == 0 else n + 1 for n in numbers]


# Кортеж (tuple) - неизменяемый список (нельзя изменять и добавлять элементы)
# В остальном работа как со списком (индексы, перебор с помощью for)

t = (3, True, "Ivan")

for elem in t:
    print(elem)