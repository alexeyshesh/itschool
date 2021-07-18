# hw 1

def gt_neighbours(numbers):
    count = 0
    for i in range(1, len(numbers)-1):
        if numbers[i-1] < numbers[i] and numbers[i+1] < numbers[i]:
            count += 1
    return count


assert gt_neighbours([1, 5, 1, 5, 1]) == 2
assert gt_neighbours([1, 2, 3, 4]) == 0
assert gt_neighbours([2, 1, 3]) == 0
assert gt_neighbours([1, 5, 1]) == 1
assert gt_neighbours([1, 2]) == 0
assert gt_neighbours([6]) == 0
assert gt_neighbours([]) == 0

# hw 2


def max_prod(numbers):
    if len(numbers) >= 4:
        (min1, min2, max2, max1) = sorted(numbers[:4])
        for n in numbers[4:]:
            if n > max1:
                max2 = max1
                max1 = n
            elif max2 < n <= max1:
                max2 = n
            elif min1 <= n < min2:
                min2 = n
            elif n < min1:
                min2 = min1
                min1 = n
        if max1 * max2 > min1 * min2:
            return max2, max1
        else:
            return min1, min2
    elif len(numbers) == 3:
        a, b, c = sorted(numbers)
        if a * b > b * c:
            return a, b
        else:
            return b, c
    elif len(numbers) == 2:
        return numbers[0], numbers[1]
    else:
        return 0, 0


assert max_prod([4, 3, 5, 2, 5]) == (5, 5)
assert max_prod([-4, 3, -5, 2, 5]) == (-5, -4)
assert max_prod([-6, -7, -3, -10]) == (-10, -7)
assert max_prod([1, 2, 3]) == (2, 3)
assert max_prod([3, 4]) == (3, 4)
assert max_prod([2]) == (0, 0)
assert max_prod([]) == (0, 0)
