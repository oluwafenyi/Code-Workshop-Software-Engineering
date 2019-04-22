"""Find specs at https://www.hackerrank.com/challenges/counting-valleys/problem
"""


def counting_valleys(n, s):
    if n in range(2, 10**6 + 1):
        val = 0
        level = 0
        for stat in s:
            if stat == 'U':
                level += 1
            else:
                level -= 1

            if level == 0 and stat == 'U':
                val += 1
        return val
