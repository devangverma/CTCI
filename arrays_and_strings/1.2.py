

def checkPermutation(str1, str2):
	
	if len(str1) != len(str2) or len(str1) == 0 or len(str2) == 0 :
		print("Not a permutation")
		return 0
	
	final = [0]*26
	
	a = []
	a+= str1
	
	for c in a:
		final[ord(c)-97] = final[ord(c)-97] + 1
		
	a = []
	a += str2
	
	for c in a:
		final[ord(c)-97] = final[ord(c)-97] - 1
	
	for c in final:
		if c != 0 :
			print("Not a permutation")
			return 0
	
	print("Permutation")
	return 0

str1 = input("Please enter string1:")
str2 = input("Please enter string2:")

checkPermutation(str1, str2)