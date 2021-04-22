# ДЗ №2

students = [
    {
        'name': "Ivan Ivanov",
        'mark': 5
    },
    {
        'name': "Stepan Stepanov",
        'mark': 3
    },
    {
        'name': "Ekaterina Tihonova",
        'mark': 4
    },
    {
        'name': "Elena Elkina",
        'mark': 5
    },
    {
        'name': "Adam Douglas",
        'mark': 4
    },
{
        'name': "Adam Adam",
        'mark': 5
    }
]

n = int(input())
res = []

for student in students:
    if student['mark'] == n:
        res.append(student['name'])

print(', '.join(res))

# ДЗ №3

weather = {
    'moscow': {
        'temperature': -42,
        'humidity': 0.56
    },
    'london': {
        'temperature': 15,
        'humidity': 0.75
    },
    'new york': {
        'temperature': 20,
        'humidity': 0.68
    }
}


def isfloat(s):  
    count_dots = 0
    for i in range(0, len(s)):
        if not s[i].isdigit() and s[i] != '.' and s[i] != '-':
            return False
        if s[i] == '-' and i > 0:
            return False
        if s[i] == '.' and i == 0 or s[i] == '.' and not s[i-1].isdigit():
            return False
        if s[i] == '.':
            if count_dots == 0:
                count_dots += 1
            else:
                return False
    return True


def view(city_name):
    city_name = city_name.lower()
    if city_name not in weather:
        return "Город не найден"

    temp = weather[city_name]['temperature']
    hum = weather[city_name]['humidity']
    msg = ''
    if temp < -30:
        msg = 'Лучше оставайтесь дома'

    res = 'Температура {}ºC, влажность {}. {}'.format(temp, hum, msg)
    return res


def edit(city_name):
    response = ''

    city_name = city_name.lower()
    if city_name not in weather:
        return "Город не найден"

    old_temp = weather[city_name]['temperature']
    old_hum = weather[city_name]['humidity']

    new_temp = input("Температура ({}): ".format(old_temp))
    if new_temp == '':
        new_temp = old_temp
    elif not new_temp.isdecimal():
        return 'Неправильное значение'
    else:
        new_temp = int(new_temp)

    new_hum = input("Влажность ({}): ".format(old_hum))
    if new_hum == '':
        new_hum = old_hum
    elif not isfloat(new_hum):
        return 'Неправильное значение'
    else:
        new_hum = float(new_hum)

    weather[city_name]['temperature'] = new_temp
    weather[city_name]['humidity'] = new_hum

    return 'Сохранено: ' + view(city_name)


while True:
    cmd = input('>> ').split()
    if cmd[0] == 'exit':
        break
    if len(cmd) != 2:
        print('Неизвестная команда')
        continue
    if cmd[0] == 'view':
        print(view(cmd[1]))
    elif cmd[0] == 'edit':
        print(edit(cmd[1]))
    else:
        print('Неизвестная команда')


# Задача. Вводятся четыре числа: координаты расположения коня на шахматной доске
# и координаты второй клетки. Нужно определить, может ли конь попасть в неё

x, y = int(input()), int(input())
a, b = int(input()), int(input())

print(abs(a - x) == 2 and abs(b - y) == 1 or abs(a - x) == 1 and abs(b - y) == 2)

# Написать программу, которая переводит число из десятичной в другую систему 
# счисления (вводятся два числа)

def digit2str(d):
    if d < 10:
        return str(d)
    else:
        return chr(ord('A') + d - 10)


n = int(input())
m = int(input())
res = ''
while n > 0:
    res = digit2str(n % m) + res
    n //= m

print(res)