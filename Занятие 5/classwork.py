# 1

count = len(input().split())

# 2

sentence = input()
last_char = sentence[-1]
last_chars = sentence[-3:]
if last_char == '!' or last_chars[0] == '!':
    print('Восклицательное')
elif last_char == '?' or last_chars[0] == '?' or sentence[-2] == '?':
    print('Вопросительное')
else:
    print('Повествовательное')

# 3

def str_to_date(date):
    date = date.split('.')
    return int(date[0]), int(date[1]), 2000 + int(date[2])


def date_to_str(date):
    return '{0}.{1}.{2}'.format(date[0], date[1], date[2])

todo_list = [
    ("Go to gym", (31, 4, 2021)),
    ("Go to library", (30, 5, 2021))
]  # (label, (day, month, year))

while True:
    cmd = input(">> ")  # add | show
    if cmd == 'add':
        label = input("What do you want to do?\n")
        date = str_to_date(input("Deadline (dd.mm.yy): "))
        todo_list.append((label, date))
    elif cmd == 'show':
        j = 1
        for todo in todo_list:
            print('{}. {} ({})'.format(j, todo[0], date_to_str(todo[1])))
            j += 1
    elif cmd == 'edit':
        num = int(input("What todo do you want to edit?\n"))
        if 0 < num <= len(todo_list):
            todo = todo_list[num - 1]
            label = input("What do you want to do? ({})\n".format(todo[0]))
            date = str_to_date(input("Deadline ({}): ".format(date_to_str(todo[1]))))
            todo_list[num - 1] = (label, date)
        else:
            print("No such todo")
    elif cmd == 'delete':
        num = int(input("What todo d oyou want to delete?\n"))
        if 0 < num <= len(todo_list):
            todo = todo_list[num - 1]
            todo_list.remove(todo)
        else:
            print("No such todo")
    elif cmd == 'exit':
        break

# Как проверить, является ли введенный символ цифрой?
# c = input()
# if c == '0' or c == '1' ...
# if c in '0123456789'
# if ord('0') <= ord(c) <= ord('9')
# if c.isdigit()

# ord() - функция, которая возвращает порядковый номер символа в кодировке
# chr() - функция, котоорая по порядковому номеру в кодировке получает символ

# Понятно, что это две обратных функции, поэтому если применить обе, то ничего
# не произойдет:

print(ord(chr(50)))

# Задача. Написать функцию, реализующую шифр Цезаря (загуглите, если не знаете, 
# что это)

def ceasar(offset, text):
    res = ""
    for c in text:
        res += chr(ord(c) + offset)
    return res

n = int(input("Offset: "))
t = input("Text: ")
print(ceasar(n, t))

"""
Словарь

{key1: value1, key2: value2, ...}


"""

# Создание словаря
cities = {
    'Москва': 23,
    'Санкт-Петербург': 10
}

print(cities['Москва'])  # квадратные скобки, чтобы получить элемент ппо ключу

cities = ['Москва', 'Новгород', 'Казань']
events = dict.fromkeys(cities, 0)  # получаем словарь из с ключами из списка, 
                                   # втоорой аргумент - значение всех элементов
print(events)

events['Казань'] = 9  # чтобы добавить новую пару ключ-значение в словарь, 
                      # используем квадратные скобки и ключ
print(events)

# Задача. Преобразовать список кортежей в словарь
students = [('Jake', 5), ('Ivan', 4), ('Elena', 3)]
# -> {'Jake': 5, 'Ivan': 4, 'Elena': 3}
res = {}
for student in students:
    res[student[0]] = student[1]

print(res)

# Удаление элементов словаря

d = {'a': [1, 2, 3], 'b': 2, 'c': 3}
print(d)

del d['b']  # удалить один элемент по ключу
print(d)

d.clear()  # полностью очистить словарь
print(d)

# В качестве ключей могут использоваться любые неизменяемые типы - числа, 
# строки, кортежи

d = {(1, 2, 3): 4}
print(d[(1, 2, 3)])

# Задача. Есть пользователи сос ледубщими характеристиками:
# admin / not admin
# gender (False - female, True - male)
# В зависимости от значений с ними надо по-разному здорооваться:
# admin -> Здравствуйте, дорогой (дорогая) администратор
# not admin -> Здравствуйте, дороогой гость (дорогая гостья)

greetings = {
    (True, True): "Здравствуйте, дорогой администратор",
    (True, False): "Здравствуйте, дорогая администратор",
    (False, True): "Здравствуйте, дорогой гость",
    (False, False): "Здравствуйте, дорогая гостья"
}

user = (False, False)

print(greetings[user])

d = {'a': [1, 2, 3], 'b': 2, 'c': 3}
print(d.get('a', 0))  # если попытаться достать элемент, которого в словаре нет,
                      # с помощью [], проограмма упадет. Длля этого есть функция 
                      # .get(), первый аргумент - ключ, второй - значение, если 
                      # такого ключа нет

# Цикл for перебирает ключи, а не значения:

d = {'a': [1, 2, 3], 'b': 2, 'c': 3}
# for key in d:
#     print(d[key])
#
print(list(d.keys()))  # .keys() - список ключей
print(list(d.values()))  # .values() - список значений

print(2 in d.values())  # проверить, что эдемент есть в словаре


# Задача. Написать функцию, которая возвращает ключ минимального элемента 
# словаря

def min_key(d):
    mk = list(d.keys())[0]
    min_value = d[mk]
    for key in d:
        if d[key] < min_value:
            mk = key
            min_value = d[key]
    return mk


d = {'a': 5, 'b': 2, 'c': 3, 'd': 10}
print(min_key(d))