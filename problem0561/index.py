from itertools import combinations

def isprime(n):
  if n < 2: return False;
  if n==2 or n==3: return True;
  if n%2==0 or n%3==0: return False;
  maxDivisor = n**0.5;
  d,i=5,2;
  while d<=maxDivisor:
    if n%d==0: return False;
    d+=i;
    i=6-i;
  return true;

def countpairsnumber(n):
  lista = combinations(range(1,n+1),2);
  result = 0;
  for x in lista:
    if n%x[0]!=0 or n%x[1]!=0:
      continue;
    elif x[1]%x[0]!=0:
      continue;
    result+=1;
  return result;

def primeproduct(n):
  result = 1;
  count=0;
  while count<=n:
    count+=1;
    if isprime(count):
      result*=count;
  return result;

def highestinteger(n):
  power = 0;
  result = 0;
  while True:
    temp = 2**power;
    if temp > n:
      break;
    if n%(temp)==0:
      result=power;
    power+=1;
  return result;

def sumator(n):
    

print("Pending to code");
pairs = countpairsnumber(6);
print("Pairs(6): "+str(pairs));
product = primeproduct(2);
print("PrimeProduct(2): "+str(product));
m = 2;
n = 1;
highest = highestinteger(countpairsnumber(primeproduct(m)**n));
print("HighestInteger("+str(m)+","+str(n)+"): "+str(highest));

print(10**12);

    