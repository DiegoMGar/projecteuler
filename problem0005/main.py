def evenlyDivisible(num,max):
	for x in range(2,max+1):
		if num%x!=0:
			return False;
	return True;

print("Testing evenly divisible: 2520, 1 to 10\n");
print(evenlyDivisible(2520,10));
input("Ready?");
print("Testing evenly divisible: X, 1 to 20\n");
num = 20;
while True:
	print(num);
	if(evenlyDivisible(num,20)):
		print("X = "+str(num));
		break;
	num+=20;