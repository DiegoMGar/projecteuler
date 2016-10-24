def primalityTest(n):
  if n <= 1: return False;
  elif n <= 3: return False;
  elif n%2 == 0 or n%3 == 0: return False;
  i=5;
  while i*i <= n:
    if n%i == 0 or n%(i+2) == 0: return False;
    i = i+6;
  return True;

def multList(lista):
  result = 1;
  for x in lista:
    result*=x;
  return result;

def getPrimeFactors(num):
  lista = [];
  i = 2;
  while True:
    if primalityTest(i):
      if num%i == 0:
        lista.append(i);
        if multList(lista)>=num:
          break;
    i+=1;
  return lista;

print("Problem 3 of Project Euler: Largest prime factor.\n");
print("\tTesting prime factors of 13195:\n");
print(getPrimeFactors(13195));
print("\n");
print("\tTesting prime factors of 600851475143:\n");
print(getPrimeFactors(600851475143));
print("\n");
print("\tEND***");