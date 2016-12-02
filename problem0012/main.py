from math import sqrt;

def triangularNumber(n):
  return int((n*(n+1))/2);

def countPairFactors(n):
  num = int(sqrt(n));
  count = 0;
  for x in range(1,num+1):
    if n%x == 0 : count+=1;
  return count*2;

print("Euler Project: Problem 12\n");
print("What is the value of the first triangle number to have over five hundred divisors?\n");
input("Ready?");
found = False;
count = 1;
tNumber = 0;
while not(found):
  tNumber = triangularNumber(count);
  numDivisors = countPairFactors(tNumber);
  #print("Num: "+str(count)+", tNumber: "+str(tNumber)+", div: "+str(numDivisors));
  found =  numDivisors >= 500;
  count+=1;
print(tNumber);
