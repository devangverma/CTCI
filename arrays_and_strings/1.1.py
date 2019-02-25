
def allUnique(str):
	a = []
	b = {}
	a+= str
	print(a) 
	
	for c in a:
		b[c] =0
		
	for c in a:
		if b[c] < 1:
			b[c]= b[c]+1
		else:
			print("Is not unique")
			return 0
	print("Is Unique")
	return 0

str = input("Please enter a string:")
allUnique(str)