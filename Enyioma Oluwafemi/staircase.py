def staircase(n):
    for i in range(n):
        print(" " * (n-i) + "#" * i)


def staircase(n):
    for i in range(n):
        print(("#"*i).rjust(n))


staircase(100)
