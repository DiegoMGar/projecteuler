if __name__ == "__main__":
    listaPotencias = []
    for a in range(2, 100 + 1):
        for b in range(2, 100 + 1):
            listaPotencias.append(a ** b)
    print(len(set(listaPotencias)))
