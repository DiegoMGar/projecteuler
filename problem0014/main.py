from time import time;
def oddCollatz(n):
  return int((3*n)+1);
def evenCollatz(n):
  return int(n/2);
def Collatz(n):
  if n<=1: return 1;
  try:
    temp = memoization[n];
    return memoization[n];
  except IndexError:
    temp=0;
  if n%2 == 0: return (1+Collatz(evenCollatz(n)));
  return (1+Collatz(oddCollatz(n)));
def CollatzProblem(max):
  i=1;
  starter=1;
  tenPercent = max//10;
  greatestChain=0;
  global memoization;
  while i<max:
    temp =  Collatz(i);
    if i<=tenPercent: memoization.append(temp);
    if temp > greatestChain: greatestChain = temp; starter=i;
    i+=1;
  return ["Starter: "+str(starter),"len: "+str(greatestChain)];
memoization = [0];
print("Euler Project: Problem 14\n");
print("Longest Collatz sequence.\n");
print("Chain starting with 13 length: "+str(Collatz(13)));
print("Which starting number, under one million, produces the longest chain?\n");
input("Ready?");
start = time();
print(CollatzProblem(1000000));
print("Time: "+str(time()-start));
