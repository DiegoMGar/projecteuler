from bisect import bisect_left
from functools import reduce


# FUNCIONES
def find_in_sorted_list(lista, elem, elems):
    i = bisect_left(lista, elem)
    return i < elems and lista[i] == elem


def es_primo(num, memoizados, cantidad):
    if find_in_sorted_list(memoizados, num, cantidad):
        print("Se ha encontrado con sorted list")
        return True
    tmp = num - 1
    while tmp > 1:
        if num % tmp == 0:
            return False
        tmp -= 1
    return True


def es_primo_truncado(num, memoizados, cantidad):
    num = str(num)
    # print(f"De {num}")
    if len(num) <= 1:
        return False
    for x in range(1, len(num)):
        # print(num[x:])
        if len(num[x:]) != len(str(int(num[x:]))):
            return False
        if not find_in_sorted_list(memoizados, int(num[x:]), cantidad):
            return False
    for x in range(1, len(num)):
        # print(num[:x])
        if len(num[:x]) != len(str(int(num[:x]))):
            return False
        if not find_in_sorted_list(memoizados, int(num[:x]), cantidad):
            return False
    return True


if __name__ == "__main__":
    print("Inicio del problema 37")
    print("Encuentra la suma de los 11 primeros que sean trucables de izquierda a derecha y de derecha a izquierda...")
    primosMemoizacion = []
    primosEncontrados = []
    init = 1
    primosContador = 0
    while primosContador < 2000:
        if es_primo(init, primosMemoizacion, primosContador):
            if es_primo_truncado(init, primosMemoizacion, primosContador):
                print("Primo trucable encontrado!")
                primosEncontrados.append(init)
                if len(primosEncontrados) >= 11:
                    # break
                    pass
            primosMemoizacion.append(init)
            primosContador += 1
        init += 1
        if init % 100 == 0:
            lenPrimosEncontrados = len(primosEncontrados)
            print(f"Iteracion {init} [{primosContador} : {lenPrimosEncontrados}]")
    print("Primos resultantes:")
    print(primosMemoizacion)
    print("\n")

    if len(primosEncontrados) < 1:
        print("No se han encontrado primos truncatables")
    else:
        print("Resultado: ")
        lenPrimosEncontrados = len(primosEncontrados)
        print(f"{primosEncontrados} => {lenPrimosEncontrados}")
        print(reduce((lambda x, y: x + y), primosEncontrados))

    print("\nFin ******")
