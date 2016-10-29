def isPalindrome(num):
	phrase = str(num);
	len = len(phrase);
	breaklen = len//2;
	for x in range(0,breaklen):
		if phrase[x]!=phrase[len-x-1]:
			return false;
		if x>=breaklen: break;
	return true;

def productCombination(digits):
	min = 10**digits;
	max = (10**(digits+1))-1;
	
	
print(isPalindrome(9009));
print("Problem 4 of Project Euler: Largest palindrome product.\n");
print("\tTesting palindrome of two 2-digit numbers:");

print("\n");
print("\tTesting palindrome of two 2-digit numbers:");

print("\n");
print("\tEND***");
