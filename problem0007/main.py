def isPrime(num):
  if num<=1: return False;
  if num<=3: return True;
  if num%2==0 or num%3==0: return False;
  i = 5;
  while i*i<=num:
    if num%i==0 or num%(i+2)==0:
      return False;
    i+=6;
  return True;

def primeAt(num):
  result = 1;
  i=2;
  count=0;
  while True:
    if isPrime(i):
      count+=1;
      result=i;
    i+=1;
    if count>=num: break;
  return result;

print("Euler project: problem 7.");
result = primeAt(6);
print("Result of the search for sixth prime: "+str(result));
input("Ready?");
result = primeAt(10001);
print("Result of the search for 10001th prime: "+str(result));
