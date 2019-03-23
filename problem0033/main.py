from __future__ import division


def remove_one_char(c, phrase):
    result = []
    eliminado = False
    for x in phrase:
        if x != c or eliminado:
            result.append(x)
        else:
            eliminado = True
    return "".join(result)


def simplify_division(numerator, denominator):
    for x in numerator:
        if x in denominator:
            denominator = remove_one_char(x, denominator)
            numerator = remove_one_char(x, numerator)
            return [numerator, denominator]
    return [numerator, denominator]


if __name__ == "__main__":
    for x in range(10, 100):
        for y in range(x + 1, 100):
            simple = simplify_division(str(x), str(y))
            if simple[0] >= simple[1] or simple[0] == 0 or simple[1] == 0 \
                    or (x / 10 == int(simple[0]) and y / 10 == int(simple[1])):
                continue
            simpleStr = "/".join(simple)
            if len(simpleStr) > 3:
                continue
            # print(x / y)
            # print(int(simple[0]) / int(simple[1]))
            if x / y == int(simple[0]) / int(simple[1]):
                print(f"{x}/{y} => ", simpleStr)
