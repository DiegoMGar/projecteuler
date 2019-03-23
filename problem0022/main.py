import os


def read_names(fichero):
    fichero = os.path.abspath(fichero)
    f = open(fichero, "r")
    nombres = f.read()
    f.close()
    nombres = map(lambda x: x.replace("\"", ""), nombres.split(","))
    nombres = list(nombres)
    nombres.sort()
    return nombres


def ordValue(nombre):
    total = 0
    for x in nombre:
        total += ord(x) - ord('A') + 1
    return total


if __name__ == "__main__":
    print("*** Problem 22 ***")
    nombres = read_names("p022_names.txt")
    length = len(nombres)
    total = 0
    for contador, current in enumerate(nombres):
        total += ((contador + 1) * ordValue(current))
    print(f"Suma total de la puntuación de nombres: {total}")
