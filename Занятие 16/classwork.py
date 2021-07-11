# hw 2

# f([1, 5, 8], [3, 10, 20]) -> [1, 3, 5, 8, 10, 20]

def merge(l1, l2):
    l3 = l1 + l2
    l3.sort()  # O((n + m) * log (n + m))
    return l3


def merge_sorted(l1, l2):  # O(n + m)
    p1 = 0
    p2 = 0
    res = []

    while p1 < len(l1) or p2 < len(l2):
        if p1 >= len(l1) or l1[p1] > l2[p2]:
            res.append(l2[p2])
            p2 += 1
        elif p2 >= len(l2) or l1[p1] < l2[p2]:
            res.append(l1[p1])
            p1 += 1

    return res


# assert -- используется для проверки, если после него стоит выражение с 
# результатом True, то ничего не происхоодит, если False, происходит ошибка
assert merge_sorted([1, 5, 10], [2, 4, 12]) == [1, 2, 4, 5, 10, 12]
assert merge_sorted([], [1, 2, 3]) == [1, 2, 3]
assert merge_sorted([], []) == []


# Задача. Вводятся числа, нужно найти минимальный четный элемент, а если его нет,
# напечатать -1

numbers = list(map(int, input().split()))
if len(numbers) > 0:
    m = -1
    for n in numbers:
        if (n < m or m % 2 == 1) and n % 2 == 0:
            m = n
    print(m)
else:
    print(-1)

# Задача. Напишите программу, которая находит в массиве элемент, самый близкий по
# величине к  данному числу.

_ = input()
numbers = list(map(int, input().split()))
target = int(input())
if len(numbers) > 0:
    closest = numbers[0]
    for n in numbers:
        if abs(target - closest) > abs(target - n):
            closest = n
    print(closest)
else:
    print('No numbers')

