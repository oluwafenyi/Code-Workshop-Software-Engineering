"""Takes in an array as input and outputs the fraction of the array which is
positive, negative and zero"""


def plus_minus(array):
    zeroes = 0
    negatives = 0
    positives = 0
    n = len(array)
    for val in array:
        if val == 0:
            zeroes += 1
        elif val < 0:
            negatives += 1
        else:
            positives += 1
    print(f"Fraction of zeroes: {zeroes / n:.6f}")
    print(f"Fraction of negatives: {negatives / n:.6f}")
    print(f"Fraction of positives: {positives / n:.6f}")


plus_minus([-1, 0, 5, 0, 0, -1, -3])
