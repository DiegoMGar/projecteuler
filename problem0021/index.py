def proper_divisor(n, m):
    return n % m == 0


def d(n):
    m = n - 1
    total = 0
    while m >= 1:
        if proper_divisor(n, m):
            total += m
        m -= 1
    return total


def are_amicable_numbers(n, m):
    return d(n) == m and d(m) == n


def is_amicable_number(n):
    m = d(n)
    return d(m) == n and n != m


if __name__ == "__main__":
    print("Problem 20 - Amicable numbers.")
    total = 0
    for n in range(1, 10000 - 1):
        if is_amicable_number(n):
            total += n
            print(n)
    print(f"Sum of amicable numbers lower than 10000: {total}")
