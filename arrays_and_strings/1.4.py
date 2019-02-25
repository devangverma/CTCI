

def palindromePermutation(str):
	
	if len(str) < 2 :
		print("Palindrome!")
		return 0
	
	final = [0]*26
	
	str_new = str.replace(" ","")

	a = []
	a+= str_new
	odds = 0
	
	for c in a:
		final[ord(c)-97] = final[ord(c)-97] + 1
		
	for c in final:
		if c%2 != 0 :
			odds = odds + 1
		
		if odds > 1 :
			print("No permutations possible.")
			return 0 
	
	print("Palindrome!")
	return 0

str = input("Please enter a string:")

palindromePermutation(str)