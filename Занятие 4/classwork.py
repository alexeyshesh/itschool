# Разбор ДЗ

# Задача 2
users = ['kitty_cat123', 'dalerdaler', 'kit_ne_kit']


def is_user(username):
    return username in users

# Задача 3

users = [
    ('Ivan', 'Ivanov'),
    ('Petr', 'Petrov'),
    ('Stepan', 'Pythonov')
]

users1 = [user[0] + ' ' + user[1] for user in users]
print(users1)

"""
Строка - набор символов, заключенный в кавычки

Например, 'cat' или "dog"
"""
# Чтобы вставлять некоторые специальные символы внутрь строки, используется \
print("hello\nworld") # перенос строки

# Если внутрь строки нужно вставить кавычки, можно всю строоку взять в кавычки 
# другого типа
print("I don't know")
print('Я пошел в ресторан "Буратино"')

# Если такой возможности нет, можно экранировать кавычки с помощью \. Тогда 
# они будут интерпретироваться как символ, а не как начало/конец строки
print('I don\'t know')
print("Я пошел в ресторан \"Буратино\"")

# Чтобы вывести сам \, его тоже нужно экранировать с помощью \
print('How to print \\?')

# Тройные кавычки используются не только для комментариев, но и для сохранения 
# переносов строки в тексте
s = """Hello
Goodbye"""
print(s)

# Строку можно воспринимать как кортеж символов, поэтому к строкам применимы 
# похожие методы работы

s = "Hello world"
print(s[3])  # индексация
print(s[::2])  # slice

for c in s:  # цикл for
    print(c)

# Пример. Посчитать количество гласных в строке

s = "Привет о чем говорите"

vowels = 'аеуыиоэёэя' # гласные буквы
amount = 0
for c in s:
    if c in vowels:  # оператор проверки наличия в строке in (как и в списке)
        amount += 1

print(amount)

# Пример. Преобразовать дату в формате dd.mm.yy в три числа

# Способ первый: slice
date = input()  # 13.06.21 -> day, month, year
date = (int(date[:2]), int(date[3:5]), 2000 + int(date[6:]))
print(date)

# Способ второй: функция split делит строку на список строк по какому-то 
# разделителю
date = input()
print([(n) for n in date.split()])


# Пример. Есть три категории постов: #usa, #news, #ipo. Нужно разделить входящие 
# соообщения по трем спискам в зависимости от тега

usa_posts = []
news_posts = []
ipo_posts = []

while True:
    msg = input()  # 'good news #usa'
    if msg == 'exit':
        break

    if '#news' in msg:
        news_posts.append(msg)
    if '#usa' in msg:
        usa_posts.append(msg)
    if '#ipo' in msg:
        ipo_posts.append(msg)

print(news_posts, usa_posts, ipo_posts, sep='\n')


s = "hello world"
print(len(s))  # длина строки
print(s.find('tt'))  # поиск индекса первого появления подстроки
                     # возвращает либо индекс, либо -1, если такой подстроки нет

# Фнкция join склеивает строки из списка строк через какую-то строку (split наоборот)
s = [str(1), '2', 'ccc']
print("---".join(s))

# Функция .format() заменяет {} в строке на свои аргументы
name = 'Ivan'
print("Hello, {}".format(name))  # Hello, Ivan

# Пример. Написать todo-list, в котором можно добавлять и просматривать записи

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
    elif cmd == 'exit':
        break



