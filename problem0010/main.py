def primalityTest(n):
  if n <= 1: return False;
  elif n <= 3: return True;
  elif n%2 == 0 or n%3 == 0: return False;
  i=5;
  while i*i <= n:
    if n%i == 0 or n%(i+2) == 0: return False;
    i = i+6;
  return True;

def sumPrimes(init,end):
  sum = 0;
  while end>init:
    if primalityTest(end):
#      print("Sumando: "+str(end));
      sum+=end;
    end-=1;
  return sum;

print("Euler Project: Problem 10");
print("Sumation of primes:");
print("The sum of the primes below 10 is: "+str(sumPrimes(1,10)));
input("Ready?");

print("Find the sum of all the primes below two million:");
print(sumPrimes(1,2000000));
