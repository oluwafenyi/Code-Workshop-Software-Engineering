
def mini_max_sum(array):
    """ Returns the highest sum and lowest sum possible for elements in the
        array.
        :params: one dimensiona, list
        :returns: (lowest sum, highest sum)
    """
    array.sort()
    return sum(array[:len(array)-1]), sum(list(reversed(array))[:len(array)-1])


print(mini_max_sum([1, 2, 3, 4, 5]))
