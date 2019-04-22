"""Takes an array(list) as input and outputs the sum of elements in that
array."""


def array_sum(array):
    return sum(array)


def array_s(array):
    total = 0
    for i in array:
        total += i
    return total


print(array_sum([1, 2, 3, 4, 5]))
print(array_s([1, 2, 3, 4, 5]))
