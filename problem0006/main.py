def sumofsquares(num):
	result = 0;
	for x in range(1,num+1):
		result+=pow(x,2);
	return result;
def squareofsum(num):
	result = 0;
	for x in range(1,num+1):
		result+=x;
	result=pow(result,2);
	return result;

print("Euler project: problem 6.");
ten = squareofsum(10)-sumofsquares(10);
print("Result of the ten first natural numbers: "+str(ten));