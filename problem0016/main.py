#!/usr/bin/python3.5
import math
print("Problema 16 del proyecto EULER")
print("Sum of the digits of 2^1000")
potencia = math.pow(2,1000)
result = 0
for x in str(int(potencia)):
    result += int(x)
print("Result: ")
print(int(result))