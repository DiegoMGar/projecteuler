def isTriplet(a,b,c):
  if not(a<b and b<c): return False;
  if not(pow(a,2)+pow(b,2)==pow(c,2)): return False;
  return True;

def isTriplet1000(a,b,c):
  if not(a<b and b<c): return False;
  if not(a+b+c==1000): return False;
  if not(pow(a,2)+pow(b,2)==pow(c,2)): return False;
  return True;

print("Euler Project: Problem 9");
print("Pythagorean triplet with 3, 4 and 5:");
print("Is 3,4,5 a Pythagorean triplet?\t"+str(isTriplet(3,4,5)));
input("Ready?");

print("Searching Pythagorean triplet that a+b+c=1000...");
a=3;
b=4;
c=5;
finded=False;
while not(finded):
  c+=1;
  b=1;
  a=1;
  while not(finded) and b<c-1:
    b+=1;
    a=1000-b-c;
    if isTriplet1000(a,b,c): print("roto"); finded=True; break;
    

print(str(a)+" + "+str(b)+" + "+str(c)+" = "+str(a+b+c));
