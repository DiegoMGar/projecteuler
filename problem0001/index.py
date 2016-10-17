sum=0;
for x in range(0,1000):
  if x%5==0 or x%3==0:
    sum+=x;
print("Total primes of 5 or 3 are in range(0,1000): "+str(sum));