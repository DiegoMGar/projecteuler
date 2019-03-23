import os
import psutil

memo = {}


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    contador = 1
    found = False
    while not found:
        tmp = fibonacci(contador)
        memo[contador] = tmp
        found = len(str(tmp)) >= 1000
        contador += 1
    print(contador - 1)
    process = psutil.Process(os.getpid())
    megabytes = process.memory_info().rss / 1000 / 1000
    print("Memory usage: {:.3f} Mb".format(megabytes))  # in bytes
