def is_product_pandigital(a, b):
    c = a * b
    d = list(str(c) + str(a) + str(b))
    d.sort()
    d = "".join(d)
    return d == "123456789"


memo = []

if __name__ == "__main__":
    total = 0
    for a in range(1, 100):
        for b in range(1, 10000):
            c = a * b
            if c in memo:
                continue
            if is_product_pandigital(a, b):
                memo.append(c)
                print(f"{a} * {b} = {c}")
                total += c
    print(f"Total del sumatorio de productos: {total}")
