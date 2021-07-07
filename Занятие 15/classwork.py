# Временная сложность - количество операций
# Пространственная сложность - объем памяти

# O - асимптотическая оценнка
# O(C) = O(1)

def check_elem(elem, lst):
    for e in lst:
        if e == elem:
            return True
    return False

# check_elem
# Если длина списка n, то в худшем случае будет сделано n сравнений
# Тогда временная сложность O(n)

def bin_check_elem(elem, lst):
    # [1, 4, 6, 7, 10]
    # 3? => центр - 6, 3 < 6 => [1, 4] => 3 < 4 => [1] => 1 != 3 => False
    lhs = 0
    rhs = len(lst) - 1
    middle = (lhs + rhs) // 2
    while rhs - lhs > 1:
        middle = (lhs + rhs) // 2
        if lst[middle] == elem:
            return True

        if lst[middle] < elem:
            lhs = middle
        elif lst[middle] > elem:
            rhs = middle


    if lst[rhs] == elem or lst[lhs] == elem:
        return True

    return False

# Худший случай - элемента нет
# Сложность - O(log(n))

a = [2, 1, 5, 9, 7, 3, 0]
print(a)

def sort_list_choice(lst):
    lst1 = lst.copy()
    res = []
    while lst1:
        m = min(lst1)
        res.append(m)
        lst1.remove(m)

    return res

# Временная сложность - O(n^2)
# Пространственная - O(n)

print(sort_list_choice(a))


def bubble_sort(lst):
    while True:
        is_sorted = True
        for i in range(1, len(lst)):
            if lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                is_sorted = False

        print(lst)

        if is_sorted:
            return lst

print('-' * 20)
print(bubble_sort(a))

# Сложность в худшем случае O(n^2)

# Лучшая сложность сортировки - O(n * log(n))

