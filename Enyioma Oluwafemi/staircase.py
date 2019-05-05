def staircase(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "#" * i)


def staircase(n):
    for i in range(1, n+1):
        print(("#"*i).rjust(n))


staircase(100)
