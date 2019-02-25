
def isSubstring(hay, needle):
	if needle in hay:
		return 1
	else:
		return 0

def stringRotation(str1, str2):
	
	new_str2 = str2+str2
	
	print("True") if isSubstring(new_str2, str1) else print("False")

str1 = input("Please enter string1:")
str2 = input("Please enter string2:")

stringRotation(str1, str2)