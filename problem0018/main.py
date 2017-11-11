#!/usr/bin/python3.5

#tupla (fila,numero)
#obtengo los números más altos de cada fila
#saco los caminos con más peso que pasen por esos números
#comparos los resultados y me quedo el mayor
#me es indiferente qué camino fue, para este problema

def path(lista):
    return false
def path_reverse(lista):
    return false

f = open("pyramid.txt")
pyramid = f.read().splitlines()
f.close()
print(pyramid)
tuplasfuertes = []
for x in pyramid:
    nums = x.split(" ")
    tuplasfuertes.append(max(nums)) #la posición en el arrray es la fila
print(tuplasfuertes)



exit()

# el codigo que hay después de este comentario
# es la primera solución que le dí, errónea
# pensando que tenía que navegar de mayor en mayor hacia abajo en la pirámide
# pero tengo que buscar el camino de mayor en toda la pirámide

result = 0
lastposition=0
for x in f.read().splitlines():
    
    if len(nums)>1:
        if nums[lastposition]<nums[lastposition+1]:
            lastposition+=1
    print(nums[lastposition])
    result += int(nums[lastposition])

print("Result: ")
print(int(result))