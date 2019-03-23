def is_product_pandigital(a, b):
    c = a * b
    d = list(str(c) + str(a) + str(b))
    d.sort()
    d = "".join(d)
    return d == "123456789"


memo = []

if __name__ == "__main__":
    total = 0
    for a in range(1, 1000):
        for b in range(1, 100000):
            pareja = [a, b]
            parejaAlternativa = [b, a]
            if pareja in memo or parejaAlternativa in memo:
                continue
            if is_product_pandigital(a, b):
                memo.append(pareja)
                print(f"{a} * {b} = {a * b}")
                total += a * b
    print(f"Total del sumatorio de productos: {total}")
    print(memo)
