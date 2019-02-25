

def oneAway(str1, str2):
	
	if abs(len(str1) - len(str2)) > 1 :
		print("Not one away.")
		return 0
	
	i = j = error = 0
	
	str1_array = []
	str2_array = []
	
	str1_array += str1
	str2_array += str2
	
	while i < len(str1) and j < len(str2):
		if error < 2:
			if len(str1) > len(str2) and str1_array[i] != str2_array[j]:
				i += 1
				error += 1
			
			elif len(str1) < len(str2) and str1_array[i] != str2_array[j]:
				j += 1
				error += 1
			elif len(str1) == len(str2) and str1_array[i] != str2_array[j]:
				i += 1
				j += 1
				error += 1
			else:
				i += 1
				j += 1
			
		else:	
			print("Not one away.")
			return 0
	
	print("One away.")
	return 0

str1 = input("Please enter string1:")
str2 = input("Please enter string2:")

oneAway(str1, str2)