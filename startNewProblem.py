import os

if __name__ == "__main__":
    currentPath = os.path.abspath(os.path.curdir)
    print("Introduce el número del ejercicio que quieres iniciar:")
    num = input()
    ejercicio = num.zfill(4)
    ejercicioDir = f"{currentPath}/problem{ejercicio}"
    if os.path.exists(ejercicioDir):
        print("El ejercicio ya existe")
        exit()
    os.mkdir(ejercicioDir)
    with open(f"{ejercicioDir}/README.md", "w") as f:
        f.write(f"# Problem {num}  \n")
    with open(f"{ejercicioDir}/main.py", "w") as f:
        f.write(f"if __name__ == \"__main__\":\n    print(\"Hello World\")\n")
    print("DONE.\n")
