
def URLify(str):
	
	a = []
	a+= str
	print("input string: ", str)
	for c in range(len(a)):
		if a[c]== ' ':
			a[c] = "%20"
	
	str = ''.join(a)
	
	print("output string: ", str)
	
	return 0

str = input("Please enter a string:")
URLify(str)