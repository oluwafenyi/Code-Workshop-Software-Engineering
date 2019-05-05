
def SherlockandSquares(start, stop):
    squares = 0
    for i in range(int(stop**0.5)):
        if i**2 in range(start, stop+1):
            squares += 1

    return squares


print(SherlockandSquares(0, 25))
