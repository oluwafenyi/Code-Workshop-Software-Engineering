"""Takes in an array as input and outputs the fraction of the array which is
positive, negative and zero"""


def plus_minus(array):
    if len(array) in range(101):
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

        print(f"{positives / n:.6f}")
        print(f"{negatives / n:.6f}")
        print(f"{zeroes / n:.6f}")


if __name__ == "__main__":
    plus_minus([-1, 0, 5, 0, 0, -1, -3])
