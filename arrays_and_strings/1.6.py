
def stringCompression(str1):
	a = []
	a+= str1
	
	new_string = ""
	previous = a[0]
	count = 0
	
	print(a) 
	
	
	for c in a:
		if previous == c:
			count+=1
		else:
			new_string += previous+str(count)
			count = 1
			previous = c
	new_string += previous+str(count)
	
	if len(new_string) < len(str1):
		print(new_string)
	else:
		print(str1)
	return 0

str1 = input("Please enter a string:")
stringCompression(str1)