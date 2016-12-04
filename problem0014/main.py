def oddCollatz(n):
  return ((3*n)+1);
def evenCollatz(n):
  return (n/2);
def Collatz(n):
  if n<=1: return 1;
  if n%2 == 0: return (1+Collatz(evenCollatz(n)));
  return (1+Collatz(oddCollatz(n)));
def CollatzProblem(max):
  i=1;
  starter=1;
  greatestChain=0;
  while i<max:
#   print("n:"+str(i));
    temp =  Collatz(i);
    if temp > greatestChain: greatestChain = temp; starter=i;
    i+=1;
  return ["Starter: "+str(starter),"len: "+str(greatestChain)];

print("Euler Project: Problem 14\n");
print("Longest Collatz sequence.\n");
print("Chain starting with 13 length: "+str(Collatz(13)));
print("Which starting number, under one million, produces the longest chain?\n");
input("Ready?");
print(CollatzProblem(1000000));
