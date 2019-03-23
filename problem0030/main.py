def is_sum_nth_powers(num):
    n = len(str(num))
    total = 0
    for x in str(num):
        total += int(x) ** n
    return num == total


def is_sum_fifth_powers(num):
    total = 0
    for x in str(num):
        total += int(x) ** 5
    return num == total


if __name__ == "__main__":
    print("Problem 30")
    total = 0
    for x in range(2, 1000000):
        if is_sum_fifth_powers(x):
            total += x
            print(x)
    print(total)
