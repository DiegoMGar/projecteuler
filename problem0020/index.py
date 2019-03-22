def factorial(num):
    if num <= 1:
        return num
    return num * factorial(num - 1)


if __name__ == "__main__":
    print("Introduce el número a calcular.")
    num = int(input())
    numFactorial = str(factorial(num))
    resultado = 0
    for n in list(numFactorial):
        resultado += int(n)
    print("La suma del factorial de {}({}) es {}".format(num, numFactorial, resultado))
